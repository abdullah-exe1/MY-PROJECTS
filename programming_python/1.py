print("start")


print("-" * 50)

while True:
    try:

        money = float(input("how much money you have: "))
        if money >= 1000 :
            print("no gift for you")
            break
        elif money <= 1000:
            print("here 1000$ for you")


    except:
        print("you didn't answr")