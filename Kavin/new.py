


def keep_going():
    pass

def add():
    first = int(input("enter number"))
    second = int(input("enter number"))
    print (f"{first} + {second} = {first + second}")

def sub(one,two):
    print (f"{one} - {two} = {one - two}")



'''
    def random():5
        print("Hello there!")
        first = randint(1,5)
        second = randint(6,9)
        print (f"{first} + {second} = {first + second}")
    '''
def main():
    add()
    for i in range(10):
        sub(100,i)

main()