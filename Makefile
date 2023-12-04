test:
	clear
	python -m unittest tests.test_data_capture.TestDataCapture.${k}

all:
	clear
	python -m unittest discover --verbose

