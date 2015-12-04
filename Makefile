check:
	flake8 test_clock.py clock.py

test: check
	py.test
