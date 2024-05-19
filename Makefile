
.PHONY: run clean

run:
	@echo "Running script with default word list..."
	python main.py

clean:
	@echo "Cleaning up..."
	del *.txt
