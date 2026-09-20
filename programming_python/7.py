amt = 0

for i in range(4):
    name = input(f"what is the name of worker {i + 1}?: ")
    print()
    age = int(input(f"what is the age of worker {i + 1}?: "))
    print

    if age <= 21:
        amt = 3000
    elif age <= 30:
        amt = 6000
    elif age == 67:
        print(" kl zg ya klb")
        amt = 0
    else:
        amt = 12000

    print(f'deer {name} your salary is {amt}')