.PHONY:run test 

run: 
	python -m compileall src/
	python -m src.main

test:
	python -m unittest discover -s tests -p "test_*.py"