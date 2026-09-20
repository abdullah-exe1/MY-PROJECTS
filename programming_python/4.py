
opt = 6767

while True:
    try:
        ans = int(input("enter the otp code: "))
        if ans == opt:
            print("correct")
            break
        else:
            print("wrong")
    except ValueError:
        print("what? Please enter numbers only.")
