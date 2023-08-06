format:
	python -m black .
	python -m isort .

lint:
	python -m black --check --diff .
	python -m isort --check --diff .

test:
	RHINO_SDK_FORBID_EXTRA_RESULT_FIELDS=1 python -m pytest -m "not local" --ignore=/out

coverage:
	RHINO_SDK_FORBID_EXTRA_RESULT_FIELDS=1 python -m coverage run \
	-m pytest  -m "not local" --ignore=/out
build:
	rm -f ./dist/*.whl
	flit build --format wheel

.PHONY: lint format test

publish:
	./dist/publish.sh

local:
	./dist/local.sh
