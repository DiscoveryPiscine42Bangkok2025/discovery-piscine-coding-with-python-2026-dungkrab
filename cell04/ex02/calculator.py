#!/usr/bin/env python3

def displayCalculator(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} + {num2} = {num1 - num2}")
    print(f"{num1} + {num2} = {int(num1 / num2)}")
    print(f"{num1} + {num2} = {num1 * num2}")

def main():
    first_num = int(input("Give me the first number: "))
    second_num = int(input("Give me the second number: "))
    print("Thank you!")
    displayCalculator(first_num, second_num)

main()