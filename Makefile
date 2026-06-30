.PHONY: setup dev build test test-all lint fmt clean

setup:
	uv sync

dev:
	uv run wcl --help

build:
	uv build

test:
	uv run python -m unittest discover -s test -p 'test_*.py'

test-all: test

lint:
	uv run python -m compileall winston bin test

fmt:
	uv run python -m compileall winston bin test

clean:
	rm -rf build dist *.egg-info .pytest_cache
