#!/usr/bin/env python3
#chmod +x password.py

def main():
    password = "Python is awesome"
    password_input = input()
    if (password_input == password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

main()