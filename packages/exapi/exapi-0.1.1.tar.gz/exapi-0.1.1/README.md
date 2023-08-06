# Exapi (Exchange API)

## Install pyenv

[pyenv-installer](https://github.com/pyenv/pyenv-installer)

```shell script
curl https://pyenv.run | bash
```

Add to ~/.profile
```shell script
if [ -d "$HOME/.pyenv" ] ; then
    export PYENV_ROOT="$HOME/.pyenv"
    command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi
```

Update
```shell script
pyenv update
```

## Install python 3.11

[pyenv](https://github.com/pyenv/pyenv)

```shell script
pyenv install 3.11.1
pyenv global 3.11.1
```

## Getting Started

### Update pip
```shell script
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
```

### Creating a virtual environment

```shell script
rm -rf venv
python3 -m venv venv
```

### Install the module in development mode
```shell script
python3 -m pip install -Ue '.[dev]'
```

## Build

```shell script
python3 -m build
# OR
hatch build
```

### Authenticate with the Package Registry

Edit the ```~/.pypirc``` file and add:

```shell
[pypi]
  username = __token__
  password = pypi-TOKEN
```

### Deploy to pypi

```shell script
python3 -m twine upload --repository pypi dist/*
```


### Clear ```__pycache__```

```shell script
py3clean .
```

## Read:
- [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
- [hatchling](https://hatch.pypa.io/latest/config/build/)
- [GitLab PyPi Repository](https://docs.gitlab.com/ee/user/packages/pypi_repository/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py)
- [Virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
