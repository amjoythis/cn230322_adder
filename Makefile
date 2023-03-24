install:
	python -m pip install --upgrade pip && python -m pip install -r requirements.txt

test:
	python -m pytest -vv test_code.py

format:
	python -m black *.py

lint:
	# python -m pylint code.py --disable=R,C
	python -m flake8 code.py --exit-zero
	#python -m flake8 code.py

all: install lint test
