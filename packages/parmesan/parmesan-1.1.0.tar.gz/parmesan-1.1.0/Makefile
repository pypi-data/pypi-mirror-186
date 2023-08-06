SETUP.PY = ./setup.py
PACKAGE_FOLDER = $(shell python3 -c 'from setuptools import find_packages;print(find_packages(exclude=["tests"])[0])')
DOCS_FOLDER = docs

.PHONY: all
all: check coverage docs

.PHONY: docs
docs:
	export PYTHONPATH=`pwd` && cd $(DOCS_FOLDER) && make html
	-xdg-open $(DOCS_FOLDER)/_build/html/index.html

.PHONY: coverage
coverage:
	coverage run --source=$(PACKAGE_FOLDER) -m tests -v
	coverage report
	coverage html
	-xdg-open htmlcov/index.html

.PHONY: check-codestyle
check-codestyle:
	pycodestyle .
	black --check .

.PHONY: check
check: coverage check-codestyle

.PHONY: clean
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf $$(find -type d -iname '__pycache__')
	rm -f $$(find -type f -iname '*.pyc')
	rm -f $(CHANGELOG_RPM)
	(cd $(DOCS_FOLDER) && make clean)
