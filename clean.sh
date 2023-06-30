#!/bin/bash

# tiny kludge utility to remove:
# cached byte code / build / lint / test tmp files
# so grepping for stuff is easier.

# NOTE: vscode and various linters wouldn't find libraries 
#       until you re-run poetry install

rm ~/git/diffant/.venv  -rf
rm ~/git/diffant/.tox   -rf
rm .mypy_cache          -rf
rm .pytest_cache        -rf
rm coverage_html_report -rf
rm .coverage            -rf
find ~/git/diffant/ -name __pycache__ -exec rm -rf {} \;
