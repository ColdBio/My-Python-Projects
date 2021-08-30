"""
A simple python calculator
""" 
def initial_values():
    print("Enter a value")
    a = int(input())
    print("Enter another value")
    b = int(input())
    print(f"The values you entered are {a} and {b}")
    print("Please enter the type of operation you would like to perform \n for example '+' denotes the addition operation")
    op = input()
    try:
        print(eval(f"a {op} b"))
    except:
        print("🚫 An error has occured, please run the program again 🚫")


initial_values()
