def get_int(prompt):
    while True:
        resp = input(prompt)
        if resp == "exit":
            exit(0)
        try:
            return int(resp)
        except:
            pass
def try_again():



def main():
    num1 = get_int("Give me a number!")
    num2 = get_int("Give me a second number!")
    ans = get_int(f"What is {num1} + {num2}")
    if ans == num1 + num2:
        print("good job")
    if not ans == num1 + num2:
        print("try again")
        get_int(f"{num1} + {num2}")
while True:
    main()
