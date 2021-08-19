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

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

pre-commit:
	poetry run pre-commit run --all-files

mypy-check:
	poetry run mypy --namespace-packages tests gendiff


.PHONY: gendiff
