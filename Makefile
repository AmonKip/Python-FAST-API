install:
	#install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python3 -m pytest -vv --cov=mylib test_*.py
build:
	#build container
deploy:
	#deploy
all: install format lint test deploy