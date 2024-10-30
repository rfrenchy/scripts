#!/bin/bash

# input: a instagram url e.g. https://www.instagram.com/p/DBTa9CtI6lj/?img_index=1

# TODO login to insta
# TODO check valid url?

# get html, wget errors if we send query params so trim them
HTML=$(wget ${1%\?*})

echo $HTML

# test () {
# }