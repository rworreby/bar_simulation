.PHONY: help run test venv install clean

help:
	@printf "Available targets:\n  make run    # run the main simulation (main.py or package)\n  make test   # run pytest\n  make venv   # create .venv and install requirements.txt (if present)\n  make clean  # remove caches and output folder\n"

run_arthur:
	bash scripts/run_arthur_strategy.sh

test:
	python -m unittest -v

venv:
	python -m venv .venv
	bash .venv/bin/activate && python -m pip install --upgrade pip setuptools wheel
	@if [ -f requirements.txt ]; then
		bash .venv/bin/activate && pip install -r requirements.txt;
	fi

install: venv

clean:
	@find . -type d -name "__pycache__" -print -exec rm -r {} + || true
	@rm -rf .pytest_cache *.pyc .output