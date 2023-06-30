## PURPOSE

Provide a cheat sheet for frequent development processes and commands.

## EXTENDING DIFFANT
To extend `diffant` to handle new file types:
1. sub class ABCDiff (copy and modify diffant/jsondiff.py )
1. in YourNewDiff sub class, override the abstract method parse_file() with code to parse a new file type into a python dictionary
1. add a file type and class name mapping to diffant/main.py:DIFF_MAPPING
1. add an `import <libaries you need>` to yournewdiff.py
1. add tests to get 100% coverage
1. get a clean `tox -qe lint ` run
1. get 100% test coverage from `coverage run -m pytest ; coverage report`
1. get a clean `tox` run to show things work in all supported python3s
1. [submit a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=cli) , you will probably have to fork the Repo.

If there is an existing library for parsing a file to a python dict, you can  get create most of the new class and associated tests by pasting diffant/diffjson.py and tests/diffyml/test_yml_parse_file.py into chat-gpt chats and ask it to create the class and tests for <your new file type> using the supplied as templates.

## SETUP FOR DEVELOPMENT
    [install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) in your user environment
 ```
    mkdir -p ~/git/
    git clone https://github.com/omacneil/diffant
    cd diffant
    poetry install  # run poetry to install dependencies inside this project
```
    [install pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv) in your $USER environment.
```
    # install python versions
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

## Linting
```
# easiest if tox is setup, see tox.ini for commands that make up 'lint'
cd ~/git/diffant
poetry shell
tox -qe lint
```
