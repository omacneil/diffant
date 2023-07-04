## PURPOSE
Provide a cheat sheet for frequent development processes and commands.

## SETUP FOR DEVELOPMENT
[install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) in your user environment
 ```mkdir -p ~/git/
git clone https://github.com/omacneil/diffant
cd diffant
 poetry install  # run poetry to install dependencies inside this project
 ```
[install pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv) in your $USER environment.
```# install python versions
# see also tox.ini:envlist
pyenv install -v 3.8.17
pyenv install -v 3.9.17
pyenv install -v 3.10.12
pyenv install -v 3.11.4
pyenv install -v 3.12.0b2

pyenv local 3.8.17 3.9.17  3.10.12 3.11.4 3.12.0b2

# you can remove installed python versions with:
rm -rf ~/.pyenv/versions/
```

## RUNNING TESTS
```
cd ~/git/diffant
poetry shell
coverage erase
coverage run -m pytest

# summary of test coverage
coverage report

# fancy/useful html report of coverage
coverage html
firefox coverage_html_report/index.html &

# run tests for all supported versions of python
tox -q
```

## LINT
```
# see tox.ini for commands that make up 'lint'
cd ~/git/diffant
poetry shell
tox -qe lint
```

## VERSIONS
There is no significance to version numbers, potentially breaking changes are noted in CHANGLELOG.md

## BRANCH / COMMIT
* Create feature branch / pull requests for non trivial changes
* Commit to main (if have rights) for doc changes
* Update CHANGELOG.md [Unreleased] as needed.

## MERGE
* Update CHANGELOG.md [Unreleased] as needed.

## RELEASING
1. Update `pyroject.toml:version =`
1. Move changes from CHANGELOG.md [Unreleased] to [version] section
1. git add pyproject.toml CHANGELOG.md
1. git commit -m 'prepare release 1.0.2'
1. `git tag -a 1.0.2 -m 'see CHANGELOG'`
1. `git push`
1. `git push origin 1.0.2 -m `
1. `poetry build`
1. Test install:
1. `pip uninstall diffant`
1. `pip install dist/<name of wheel>`
1. get API token from [pypi.org](https://pypi.org)
  - account settings
  - scroll to 'Add API token'
  - set token name: to 'diffant-<new version>' (example diffant-1.02)
  - set scope to 'project: diffant'
  - add token
  - copy token
1. Tell poetry what the API token is:`poetry config pypi-token.pypi <token text>`
1. Publish package: `poetry publish`
1. Remove the token (click remove token button in pypi.org web page)
