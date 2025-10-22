.PHONY: help run_arthur run_naive run_bell test install clean

VENV = .venv
PYTHON = $(VENV)/bin/python
RUN = source $(VENV)/bin/activate;
SHELL := /bin/bash


help:
	@printf "Available targets:\n  make run    # run the main simulation (main.py or package)\n  make test   # run pytest\n  make venv   # create .venv and install requirements.txt (if present)\n  make clean  # remove caches and output folder\n"

run_arthur: $(VENV)/bin/activate
	$(RUN) bash scripts/run_arthur_strategy.sh

run_naive: $(VENV)/bin/activate
	$(RUN) bash scripts/run_naive_strategy.sh

run_bell: $(VENV)/bin/activate
	$(RUN) bash scripts/run_naive_strategy.sh

test: $(VENV)/bin/activate
	$(PYTHON) -m unittest -v

install:
	python -m venv $(VENV)
	$(PYTHON) .venv/bin/activate && python -m pip install --upgrade pip setuptools wheel
	@if [ -f requirements.txt ]; then
		$(PYTHON) -m pip install -r requirements.txt;
	fi

clean:
	@find . -type d -name "__pycache__" -print -exec rm -r {} + || true
	@rm -rf .pytest_cache *.pyc .output