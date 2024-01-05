dar =int (input("type a number"))
for x in range (2,dar):
    if dar % x==0:
        print("the number is composite")
        exit()
print("your number is prime")