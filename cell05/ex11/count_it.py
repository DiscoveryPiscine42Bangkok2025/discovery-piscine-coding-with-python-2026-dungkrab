#!/usr/bin/env python3
import sys

def main():
    if (len(sys.argv) == 1):
        print("none")
        return
    args = sys.argv[1:]
    
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")

main()