#!/usr/bin/env python3
#chmod +x isneg.py

def main():
    try:
        value = int(input())
        if (value < 0):
            print("This number is negative")
        elif(value > 0):
            print("This number is positive")
        else:
            print("This number is both positive and negative")

    except:
        print("This is not a number")

main()