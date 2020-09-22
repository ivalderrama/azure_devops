hello:
	echo "This is my 1st make command"
install:
	pip install --upgrade pip && \
		pipinstall -r requirements.txt
lint:
	pylint --disable=R,C,E1120 hello.py
test:
	python -m pytest -vv test_adder.py
	python -m pytest -vv test_hello.py