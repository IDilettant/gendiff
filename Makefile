install:
		poetry install

build:
		poetry build

gendiff:
		poetry run gendiff -h

publish:
		poetry publish --dry-run

lint:
		poetry run flake8 gendiff

package-install:
		python3 -m pip install --user dist/*.whl


.PHONY: gendiff
