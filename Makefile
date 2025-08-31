.PHONY: install dev-install build publish package-install lint test coverage

install:
	uv pip install -e .

dev-install:
	uv pip install -e ".[dev]"

build:
	uv build

publish:
	uv publish --dry-run

package-install: build
	python3 -m pip install --user dist/*.whl

lint: dev-install
	uv run flake8 gendiff

test: dev-install
	uv run pytest --cov=gendiff --cov-report=xml --cov-report=term tests/

coverage: dev-install
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml --cov-report=term tests/

all: install dev-install

clean:
	rm -rf build dist .coverage coverage.xml .pytest_cache
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -exec rm -rf {} +
