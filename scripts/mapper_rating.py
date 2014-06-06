#!/usr/bin/env python

import sys

#file containing artistId and artistNames


def read_input(file):
    for line in file:
        # split the line into userId, artistId and artistrating by user
	userId, artistId , rating  = line.split()
        yield artistId, rating

def main():
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for artistId, rating in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
	print artistId, rating
	

if __name__ == "__main__":
    main()



