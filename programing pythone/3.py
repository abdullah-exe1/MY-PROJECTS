print("start")


print("-" * 50)

while True:
    try:

        money = str(input("do you have money : "))
        if money.lower("yes") :
            print("no gift for you")
            break
        elif money.lower("no") == "no":
            print("you're not allowed to get in")


    except:
        print("you didn't answr")