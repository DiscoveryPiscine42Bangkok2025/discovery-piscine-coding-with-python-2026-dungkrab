#!/usr/bin/env python3

def main():
    user_input = input("What you gotta say? : ")
    while(True):
        user_input = input("I got that! Anything else? : ")
        if (user_input == "STOP"):
            break
        
main()