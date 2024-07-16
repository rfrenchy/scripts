setup-python-linux:
	sudo apt install pipx
	pipx install pipenv

# remove yellow parts from my cv generated by otta
remove-yellow:
	pipenv run python3 remove-yellow.py otta.pdf ryan-cv.pdf

# install pdf modules for remove-yellow script
install-yellow-modules:
	pipenv install PyMuPDF
