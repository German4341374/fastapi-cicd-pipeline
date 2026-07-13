SHELL := /bin/bash
PYTHON ?= python3
VENV := .venv

.PHONY: setup format lint test audit build up down clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --disable-pip-version-check -e '.[dev]'

format:
	$(VENV)/bin/ruff format .

lint:
	$(VENV)/bin/ruff format --check .
	$(VENV)/bin/ruff check .

test:
	$(VENV)/bin/pytest tests --cov=app --cov-report=term-missing

audit:
	$(VENV)/bin/pip-audit

build:
	docker build --target production -t pipeline-demo-api:local .

up:
	docker compose up --build -d

down:
	docker compose down

clean:
	docker compose down --remove-orphans 2>/dev/null || true
	rm -rf $(VENV) .pytest_cache .ruff_cache .coverage coverage.xml *.egg-info
