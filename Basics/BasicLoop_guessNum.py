number= 10
count= 0
limit= 3
while int(count) < int(limit):
    guess= int(input("guess= "))
    count+=1
    if guess == 10:
        print(f"you won , the secret number is {number}")
        break
    elif count==limit:
        print(f"you lost,   the secret number was {number} ")
