def input_numbers():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    return a,b

def add(argument1, argument2):
    summation=0
    summation=argument1+argument2
    return summation

def display(a,b,summation):
    print(summation)


def main():
    a, b = input_numbers()
    summation = add(a, b)
    display(a, b, summation)
