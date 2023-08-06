.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/flake8: ## check style with flake8
	flake8 --max-line-length 88 --extend-ignore E203 lyceum tests

lint/black: ## check style with black
	black --check lyceum tests

lint: lint/flake8 lint/black ## check style

format:
	isort lyceum tests && black lyceum tests

format/watch:
	watchmedo shell-command -p '*.py' -c '$(MAKE) format' -R -D .

test: ## run tests quickly with the default Python
	pytest

test/watch: # TODO only the changed file
	watchmedo shell-command -p '*.py' -c 'pytest ${watch_object}' -R -D .

test-all: ## run tests on every Python version with tox
	tox

dev:
	$(MAKE) -j 2 format/watch test/watch	

coverage: ## check code coverage quickly with the default Python
	coverage run --source lyceum -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/lyceum.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ lyceum
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

docs/watch: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: ## package and upload a release
	flit publish

install: clean ## install the package to the active Python's site-packages
	python setup.py install
