import importlib.util
import shutil
import sys
import typing as t
from pathlib import Path
from types import ModuleType
from uuid import uuid1 as uuid

import rich_click as click
import typed_settings as ts
import yaml
from jinja2 import Environment, FileSystemLoader
from rich import print

from makejinja.types import ExportsTemplate

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from makejinja.config import OPTION_GROUPS, Config

click.rich_click.USE_MARKDOWN = True
click.rich_click.OPTION_GROUPS = OPTION_GROUPS


def _import_module(path: Path) -> ExportsTemplate:
    # https://stackoverflow.com/a/41595552
    # https://docs.python.org/3.11/library/importlib.html#importing-a-source-file-directly
    name = str(uuid()).lower().replace("-", "")

    if path.is_dir():
        path /= "__init__.py"

    spec = importlib.util.spec_from_file_location(name, path)
    assert (
        spec is not None
    ), f"The module has not been found. Please verify the given path '{path}'."

    module: ModuleType = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None

    spec.loader.exec_module(module)

    return module.Exports()


def _from_yaml(path: Path) -> dict[str, t.Any]:
    data = {}

    with path.open("rb") as fp:
        for doc in yaml.safe_load_all(fp):
            data.update(doc)

    return data


def _from_toml(path: Path) -> dict[str, t.Any]:
    with path.open("rb") as fp:
        return tomllib.load(fp)


DATA_LOADERS: dict[str, t.Callable[[Path], dict[str, t.Any]]] = {
    ".yaml": _from_yaml,
    ".yml": _from_yaml,
    ".toml": _from_toml,
}


def _collect_files(paths: t.Iterable[Path], pattern: str = "**/*") -> t.List[Path]:
    files = []

    for path in paths:
        if path.is_dir():
            files.extend(
                file
                for file in sorted(path.glob(pattern))
                if not file.name.startswith(".") and file.is_file()
            )
        elif path.is_file():
            files.append(path)

    return files


_loader = ts.default_loaders(
    appname="makejinja", config_files=(Path(".makejinja.toml"),)
)


@click.command("makejinja")
@ts.click_options(Config, _loader)
def main(config: Config):
    """makejinja can be used to automatically generate files from [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/templates/).

    Instead of passing CLI options, you can also write them to a file called `.makejinja.toml` in your working directory.
    **Note**: In this file, options may be named differently.
    Please refer to the file [`makejinja/config.py`](https://github.com/mirkolenz/makejinja/blob/main/makejinja/config.py) to see their actual names.
    You will also find an example here: [`makejinja/tests/data/.makejinja.toml`](https://github.com/mirkolenz/makejinja/blob/main/tests/data/.makejinja.toml).
    """
    modules = [_import_module(mod) for mod in config.modules]

    extensions: list[t.Any] = [*config.extensions]

    for mod in modules:
        if hasattr(mod, "extensions"):
            extensions.extend(mod.extensions())

    env = Environment(
        loader=FileSystemLoader(config.input_path),
        extensions=extensions,
        keep_trailing_newline=config.keep_trailing_newline,
        trim_blocks=config.trim_blocks,
        lstrip_blocks=config.lstrip_blocks,
        block_start_string=config.delimiter.block_start,
        block_end_string=config.delimiter.block_end,
        comment_start_string=config.delimiter.comment_start,
        comment_end_string=config.delimiter.comment_end,
        variable_start_string=config.delimiter.variable_start,
        variable_end_string=config.delimiter.variable_end,
    )

    data: dict[str, t.Any] = {}

    for path in _collect_files(config.data_paths):
        if loader := DATA_LOADERS.get(path.suffix):
            data.update(loader(path))

    for mod in modules:
        if hasattr(mod, "globals"):
            env.globals.update({func.__name__: func for func in mod.globals()})

        if hasattr(mod, "filters"):
            env.filters.update({func.__name__: func for func in mod.filters()})

        if hasattr(mod, "data"):
            data.update(mod.data())

        if hasattr(mod, "setup_env"):
            mod.setup_env(env)

    if config.output_path.is_dir():
        print(f"Remove '{config.output_path}' from previous run")
        shutil.rmtree(config.output_path)

    if config.copy_tree:
        print(f"Copy file tree '{config.input_path}' -> '{config.output_path}'")
        shutil.copytree(config.input_path, config.output_path)

    config.output_path.mkdir(parents=True, exist_ok=True)

    for input_path in config.input_path.glob(config.input_pattern):
        if not input_path.is_dir():
            relative_path = input_path.relative_to(config.input_path)
            output_path = config.output_path / relative_path
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if relative_path.suffix == config.jinja_suffix:
                template = env.get_template(str(relative_path))

                # Remove the copied file if the tree has been duplicated
                if config.copy_tree:
                    output_path.unlink()

                if not config.keep_jinja_suffix:
                    output_path = output_path.with_suffix("")

                rendered = template.render(data)

                # Write the rendered template if it has content
                # Prevents empty macro definitions
                if rendered.strip() == "" and not config.keep_empty:
                    print(f"Skip '{input_path}'")
                else:
                    print(f"Render '{input_path}' -> '{output_path}'")
                    with output_path.open("w") as f:
                        f.write(rendered)

            elif not config.copy_tree:
                print(f"Copy '{input_path}' -> '{output_path}'")
                shutil.copy2(input_path, output_path)


if __name__ == "__main__":
    main()
