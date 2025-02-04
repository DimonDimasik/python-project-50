install:
	poetry install

gendiff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
    poetry run pytest --cov=gendiff --cov-report=xml tests/

coverage:
    poetry run pytest --cov=gendiff --cov-report=term-missing tests/

