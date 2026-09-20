import math as mt

while True:

    try:


        x = float(input("enter the x value?:"))
        break
    except:
        print("the value of x isn't")


while True:

    try:


        y = float(input("enter the y value?:"))
        break
    except:
        print("the value of y isn't")


list_operations = ["+", "-", "x", "^", "/", "sqrt_of_x", "sqrt_of_y"]

print(list_operations)
while True:
    try:
        a = input("what operation do you want to use?: ")

        if a == "+":
            r = x + y
            break
        elif a == "-":
            r = x + y
            break
        elif a == "x":
            r = x * y
            break
        elif a == "^":
            r = x ** y
            break
        elif a == "/":
            r = x / y
            break
        elif a == "sqrt_of_x":
            r = mt.sqrt(x)
            break
        elif a == "sqrt_of_y":
            r = mt.sqrt(y)
            break
        else:
            print("the operation isn't valid")
    except:
        print("the operation isn't valid")
print(f'your answer is:{r}')
