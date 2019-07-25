#!/usr/bin/python
def help():
    print("\nThing Finder v1.0.0\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public Licence as published by the Free Software Foundation, etiher version 3 of License, or (at your option) any later version.\n\nhelp: Get this help screen\nfind: Find a thing\nexit: Exit this program\n")
def result1():
    print("\nShaggy is in Shaggytown, USA.\nThanks for using Thing Finder\n")
    prompt()
def result2():
    print("\nMoto Moto is in Random City, USA\nThanks for using Thing Finder\n")
    prompt()
def result3():
    print("\nGloria is in Shrek Swamp, USA\nThanks for using Thing Finder\n")
    prompt()
def find1():
    find = input("Put a thing you want to find here: ")
    if find == 'Shaggy' or find == 'shaggy':
        result1()
    if find == "Moto Moto" or find == "moto moto":
        result2()
    if find == "Gloria" or find == "gloria":
        result3()
    if find == "back" or find == "Back":
        prompt()
    else:
        print("\nThing Finder has not found anybody under that name, Please try again or type back to go back\n")
        find1()
print("Welcome to Thing Finder.")
print("This is free software released under the GNU GPL 3.0")
print("Type help to get a help message\n")
def prompt():
    command = input("# ")
    if command == 'help' or command == 'Help':
        help()
        prompt()
    if command == "exit" or command == "Exit":
        exit()
    if command == "find" or command == "Find":
        find1()
    else:
        print("\nError: Thing Finder has been looking and has not found any commands under that name. Please try again\n")
        prompt()
prompt()
