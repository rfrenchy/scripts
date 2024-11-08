# only works on Linux/WSL
install:
	sudo apt install build-essential -y
	sudo apt install meson ninja-build -y
	sudo apt install lua5.1 -y
	sudo apt install luarocks -y
	sudo apt install luajit -y
	sudo apt install libmagickwand-dev -y
	sudo apt install libgraphicsmagick1-dev -y
	sudo luarocks install magick 

	# TODO may need to build from source on windows for cffi-lua because of meson issues
	sudo luarocks install cffi-lua

run:
	luajit insta-resize.lua 004.bmp
