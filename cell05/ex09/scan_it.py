#!/usr/bin/env python3
import sys, re
def main():
    args = sys.argv[1:]
    
    if (len(args) == 2):
        keyword = args[0]
        sentence = args[1]
        matchs = re.findall(keyword, sentence)
        print(len(matchs))
    else:
        print("none")

main()