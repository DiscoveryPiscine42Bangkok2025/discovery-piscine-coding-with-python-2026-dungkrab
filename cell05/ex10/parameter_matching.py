#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    
    if (len(args) == 1):
        keyword = args[0]
        word = input("What was the parameter? ")

        if (word == keyword):
            print("Good job!")
        else:
            print("Nope, sorry...")

    else:
        print("none")

main()