from a import *

tabr = {}

while True:
    op = input("add, remove, print, and exit, choice one: ")
    if(op == "add"):
        a = input("first name: ")
        c = input("last name: ")
        b = input("phne num: ")
        if(b.isdigit() and len(b) >= 10):
            name = a,c
            add(tabr,b,name)
            print(b,"has been added")
        else:
            print(f"your phone number '{b}' is not a valid phone numbers")
    elif(op == "remove"):
        b = input("input phone number you wanna remove: ")
        if(b in tabr):
            print(remove(tabr,b))
        else:
            print("try again")
    elif(op == "print"):
        print(prunt(tabr))
    elif(op == "exit"):
        break