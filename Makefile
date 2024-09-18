install-hooks:
	poetry run pre-commit install

format-lint:
	poetry run pre-commit run --all-files