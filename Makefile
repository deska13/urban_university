install-hooks:
	pre-commit install

format-lint:
	pre-commit run --all-files