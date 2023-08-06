.PHONY: install
install:
	pip3 install -U -e .[dev]
	pip3 --version

.PHONY: clean
clean:
	rm -rf dist/ build/ well-being-diary.egg-info/ .pytest_cache/

.PHONY: build-pypi-test
build-pypi-test:
	make clean
	make install
	python3 -m build
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	python3 -m webbrowser -t "https://test.pypi.org/project/well-being-diary"
# pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ remembering==[version] -v --upgrade

.PHONY: build-pypi-live
build-pypi-live:
	make clean
	make install
	python3 -m build
	python3 -m twine upload dist/*
	python3 -m webbrowser -t "https://pypi.org/project/well-being-diary/"
