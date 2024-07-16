#! /bin/bash

## deps:
## brew install inotify-tools
## brew install eza


# TODO add $1 (ignored) to inotifywait ignore list

clear; eza --tree --level 4 -I="$1"

inotifywait -q -m -r -e 'move,create,delete' $(pwd) | \
        while read x; do
                clear; eza --tree --level 4 -I="$1"
        done
