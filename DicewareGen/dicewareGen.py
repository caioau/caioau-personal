#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Generates some random words (using the cryptographically secure generator) to be used on diceware method

usage: ./dicewareGen.py [number of words (optional)] , the default number of words is 6. 

@author: caioau@euler

@license: GPLv3+
"""

from random import SystemRandom as cryptogen
from sys import argv
import string


def main():
    n = 6
    if len(argv) > 1: # detect if the number of words is passed throuth argv
        n = int(argv[1])
    print "n=%d\n" % n
    res = GenDiceware('7776palavras.txt', n)  # default file with word list (pt-br)
    print ' '.join(res)
    print GenNumAndSpe(2 * n)


def GenDiceware(filename, n=6):
    with open(filename) as f:
        words = [line.strip() for line in f]
    return [cryptogen().choice(words) for _ in range(n)]


def GenNumAndSpe(n=12):
    charset = string.digits + string.punctuation
    return ' '.join(cryptogen().choice(charset) for _ in range(n))


if __name__ == '__main__':
    main()
