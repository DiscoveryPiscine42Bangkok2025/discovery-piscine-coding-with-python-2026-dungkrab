#!/usr/bin/env python3

def main():
    number = int(input("Enter a number\n"))
    for i in range(10):
        mult = i * number
        print(f"{i} x {number} = {mult}")

main()