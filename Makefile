SHELL := /bin/bash

build:
	./.venv/bin/python3 main.py

venv: requirements.txt
	source ./.venv/bin/activate; \
	pip3 install -r requirements.txt

clean:
	rm -rf .venv
