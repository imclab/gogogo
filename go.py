#!/usr/bin/env python
import sys
from gogogo import BoardState

def main(self, *args):
    board = BoardState('Black', 'White')
    print "Board: ", board

if __name__ == "__main__":
    main(sys.argv[0], *sys.argv[:1])