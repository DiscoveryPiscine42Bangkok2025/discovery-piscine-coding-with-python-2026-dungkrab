#!/usr/bin/env python3
#chmod +x iszero.py

def main():
    value = input()

    try:
        number = int(value)
        if number == 0:
            print("This number is equal to zero.")
        else: 
            print("This number is different from zero.")
    except:
        print("This is not a number.")

main()