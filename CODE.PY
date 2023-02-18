import random
dice=True
def roll_the_dice(dice):
    while dice:
        roll=(random.randint(1,6))
        print("Rolling",roll)
        result=input("Want to roll dice again (y/n): ")
        if result == "y":
            continue
        else:
            break

roll_the_dice(dice)


