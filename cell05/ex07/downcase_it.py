#!/usr/bin/env python3
import sys

def main():
    params = len(sys.argv) - 1
    if (params == 1):
        print(sys.argv[1].lower())
    else:
        print("none")

main()