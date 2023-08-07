#!/usr/bin/env python3

import sys

def nwordlist(min_n, max_n, o_file):

    with open(o_file, 'w') as f:
        for num in range(min_n, max_n + 1):
            f.write(str(num)) + '\n'

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 nwordlist.py <min length> <max legth> <output file>")
        sys.exit(1)

    min_n = sys.argv[1]
    max_n = sys.argv[2]
    o_file = sys.argv[3]

    nwordlist(min_n, max_n, o_file)
