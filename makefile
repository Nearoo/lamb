
setup:
	python3 -m pip install --upgrade setuptools wheel twine

build: lamb/* setup.py
	rm -rf dist/*
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*