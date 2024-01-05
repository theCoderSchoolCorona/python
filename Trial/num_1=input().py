import random

def main():
    var = random.randint(1,2)
    if var == 1:
        set var ("+")
    check =0
    sum = 0
    while(True):
        if check == 0:
            check = 1
            num_1=ask("enter number")
            num_2=ask("enter number")
            sum=(int(num_1)var int(num_2))
        ans=int(ask ("enter the answer"))
        if (ans==sum):
            print("correct")
            check = 0
        if (ans<sum):
            print("greater")
        if(ans>sum):
            print("less")






def ask(prompt):
    while (True):
        ret = input(prompt)
        if ret.lower() == "exit":
            exit()
        try:
            return int(ret)
        except:
            print("Input must be an integer!\n",prompt)






main()