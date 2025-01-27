install:
	poetry install

gendiff:
	poetry run gendiff gendiff/file1.json gendiff/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov=tests --cov-report=xml
