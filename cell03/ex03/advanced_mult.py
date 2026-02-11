#!/usr/bin/env python3
import sys

def printTables():
    num = 0
    while (num <= 10):
        print(f"Table de {num}:", end=" ")
        
        mult_num = 0
        while (mult_num <= 10): 
            print(mult_num * num, end=" ")
            mult_num += 1

        print()
        num += 1
        
def main():
    if (len(sys.argv) == 1):
        printTables()
    elif (len(sys.argv) > 1):
        print("none")

main()