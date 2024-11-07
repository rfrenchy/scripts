# only works on Linux/WSL
install:
	sudo apt install build-essential -y
	sudo apt install meson ninja-build -y
	sudo apt install lua5.1 -y
	sudo apt install luarocks -y
	sudo apt install luajit -y
	sudo apt install libmagickwand-dev -y
	sudo luarocks install magick 
	sudo luarocks install cffi-lua

run:
	luajit insta-resize.lua
