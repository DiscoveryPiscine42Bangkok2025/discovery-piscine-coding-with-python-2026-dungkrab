#!/usr/bin/env python3
import sys

def main():
    params = len(sys.argv) - 1
    args = sys.argv[1:]
    if (params >= 2):
        args.reverse()
        for text in args:
            print(text)
    else:
        print("none")

main()