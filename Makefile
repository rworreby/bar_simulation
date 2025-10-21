.PHONY: help run test venv install clean

help:
	@printf "Available targets:\n  make run    # run the main simulation (main.py or package)\n  make test   # run pytest\n  make venv   # create .venv and install requirements.txt (if present)\n  make clean  # remove caches and output folder\n"

run:
	@if [ -f main.py ]; then \
		python main.py; \
	elif [ -f bar_simulation/__main__.py ]; then \
		python -m bar_simulation; \
	else \
		printf "No entrypoint found. Add a main.py or package __main__.py. Run tests with 'make test'.\n"; \
		exit 1; \
	fi

test:
	python -m unittest -v

venv:
	python -m venv .venv
	source .venv/bin/activate && python -m pip install --upgrade pip setuptools wheel
	@if [ -f requirements.txt ]; then \
		. .venv/bin/activate && pip install -r requirements.txt; \
	fi

install: venv

clean:
	@find . -type d -name "__pycache__" -print -exec rm -r {} + || true
	@rm -rf .pytest_cache *.pyc .output