# Coder Dojo (Ham/Kingston) Common Python Packages

Basic packages containing all the Python dependencies for the Coder Dojo Sessions.

## Installation

You can install the package from GitHub using the following command.

```shell
pip install 'coder_dojo_common_python[games,data] @ https://github.com/Stedders/coder-dojo-common-python/releases/download/v0.0.1/coder_dojo_common_python-0.0.1-py3-none-any.whl'
```

This will install the games and data packages for the v0.0.1 release.

As packages are updated or new packages added a new version will be published, please check the latest version
at https://github.com/Stedders/coder-dojo-common-python/releases.

## Development

Requires poetry.

### Install

```shell
poetry install
```

### Add package

All packages are added as optional and grouped into extras.

```shell
poetry add requests --optional
```

You will then need to update the extra information to ensure the package is in the correct group.

Either update the appropriate extras section or create a new section under extras in
the [pyproject.toml](pyproject.toml) file.

```toml
[tool.poetry.dependencies]
#...stuff...
requests = { version = "^2.28.2", optional = true } # Package added as optional
#...more stuff...

[tool.poetry.extras]
#...existing extras...
web = ["requesets"] # A new extra 'web'
```