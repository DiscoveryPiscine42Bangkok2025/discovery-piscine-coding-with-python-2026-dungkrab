#!/usr/bin/env python3
import sys

def main():
    params = len(sys.argv) - 1
    if (params > 0):
        print(sys.argv[1])
    else:
        print("none")

main()