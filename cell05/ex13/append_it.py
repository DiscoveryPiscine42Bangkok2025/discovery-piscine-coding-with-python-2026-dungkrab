#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    if (len(args) < 1):
        print("none")
        return
    
    for arg in args:
        if (len(arg) > 3 and arg[len(arg) - 3:] == "ism"):
            continue
        print(arg + "ism")

main()