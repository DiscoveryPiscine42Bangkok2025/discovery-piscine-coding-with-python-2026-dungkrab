#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    if (len(args) != 1):
        print("none")
        return
    result = ""
    words = args[0].split(" ")
    for word in words:
        if (word.count("z")):
            result += "z"

    print(result)

main()
    