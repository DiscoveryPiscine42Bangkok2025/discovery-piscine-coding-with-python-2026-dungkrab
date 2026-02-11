#!/usr/bin/env python3

def checkNumberType(num):
    num_float = float(num)
    if (num_float.is_integer()):
        print("This number is integer.")
    else:
        print("This number is decimal.")

def main():
    num = input("Give me a number: ")
    checkNumberType(num)
    
main()