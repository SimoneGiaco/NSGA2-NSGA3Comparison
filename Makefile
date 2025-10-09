install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

testing:
	python -m pytest -vv --cov=main test_file.py

format:	
	black *.py 

lint:
	pylint --disable=R,C *.py

all: install lint testing format 