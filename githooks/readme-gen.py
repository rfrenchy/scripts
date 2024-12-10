
import argparse

argp = argparse.ArgumentParse("readme-gen")

# how to pass multiple lines of text to a python program from `find` command...
argp.add_argument("-p", "--prorgrams",
                  help="the list of programs to generate readme segments for")


args = argp.parse_args()
