all: test

venv:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip3 install -r requirements.txt; \

release: dist
	pytyhon3 -m twine upload -r pypi dist/scanplan-lidar-toolkit-*

install: dist
	pip3 install dist/scanplan-lidar-toolkit-*

dist: test
	python3 setup.py sdist

test: clean
	pip3 install -r requirements.txt
	pip3 install -r tests/requirements.txt
	python -m pytest -v -s --cov scanplan-lidar-toolkit --cov-report=html --cov-report=term

clean: uninstall
	-rm -rf dist
	-rm -rf scanplan-lidar-toolkit.egg-info
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf .cache
	-rm -rf .pytest_cache
	-rm -rf .venv

uninstall:
	-pip3 uninstall scanplan-lidar-toolkit -y