.PHONY:run_example test_example 

run_usecase: 
	python -m compileall usecase/src/
	python -m usecase.src.main

test_usecase:
	python -m compileall usecase/src/ usecase/tests
	python -m unittest discover -s usecase/tests -p "test_*.py"

run_example: 
	python -m compileall example/src/
	python -m example.src.main

test_example:
	python -m compileall example/src/ example/tests
	python -m unittest discover -s example/tests -p "test_*.py"