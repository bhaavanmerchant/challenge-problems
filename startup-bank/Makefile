SHELL := /bin/bash

run:
	cat sample/input.json | python nest.py currency country city

test:
	python -m unittest tests/test_transformer.py

prepare-server:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

start-server:
	export FLASK_APP=server/app.py
	python -m flask run

clean:
	deactivate
	rm -rf venv