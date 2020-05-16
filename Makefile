.PHONY: test install requirements deploy release-test
test:
	pytest -v

deploy:
	rm -f ./dist/*
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

install: requirements

requirements: .requirements.txt

.requirements.txt: requirements.txt
	pip install --upgrade pip setuptools
	pip install -r requirements.txt
	pip freeze > .requirements.txt