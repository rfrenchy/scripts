# assumes running on windows and scoop package manager install 
install:
	scoop install main/go
	go get -u github.com/urfave/cli/v2@latest
	go get -u github.com/chromedp/chromedp

insta-grab:
	go run insta-grab/insta-grab.go

setup-python-linux:
	sudo apt install pipx
	pipx install pipenv

# remove yellow parts from my cv generated by otta
remove-yellow:
	pipenv run python3 remove-yellow.py otta.pdf ryan-cv.jpeg

# install pdf modules for remove-yellow script
install-yellow-modules:
	pipenv install PyMuPDF
