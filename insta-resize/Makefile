# only works on Linux/WSL
install:
	sudo apt install build-essential
	sudo apt install meson ninja-build
	sudo apt install lua5.1
	sudo apt install luarocks
	sudo apt install luajit
	sudo apt install libmagickwand-dev
	sudo luarocks install magick
	sudo luarocks install cffi-lua

run:
	lua insta-resize.lua
