#!/usr/bin/env python3
#chmod +x mult.py

def main():
    try :
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        mult_num = first_num * second_num
        print(f"{first_num} x {second_num} = {mult_num}")
        
        if (mult_num > 0):
            print("The result is positve.")
        elif (mult_num < 0):
            print("The result is negative.")
        else:
            print("The result is positive and negative.")
    except:
        print("This is not a number.")

main()