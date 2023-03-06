def letsFindWeird(givenInt: int):
    if (givenInt % 2) != 0:
        print("Weird")
    elif (givenInt % 2) == 0 and givenInt in range(2, 6):
        print("Not Weird")
    elif (givenInt % 2) == 0 and givenInt in range(6, 21):
        print("Weird")
    elif (givenInt % 2) == 0 and givenInt > 20:
        print("Not Weird")

    else:
        print("invalid Input")


letsFindWeird(2)
