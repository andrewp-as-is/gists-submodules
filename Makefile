all:
	bash -l -c 'python3 .scripts/data.py' # -l include env
	python3 .scripts/submodules.py
