install:
	uv pip install -r requirements.txt

build:
	uv build

publish:
	uv publish -- --dry-run

package-install: build
	python3 -m pip install --user dist/*.whl

lint: dev-install
	uv run flake8 gendiff

test: dev-install
	uv run pytest --cov=gendiff --cov-report=xml tests/

coverage: dev-install
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
