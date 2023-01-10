weight = int(input("weight= "))
Lbs_kgs = input("lbs or kgs? ")
if Lbs_kgs == "lbs":
    print("your weight in kg is " , weight*0.45)

elif Lbs_kgs == "kgs":
    print(f" your weight is lbs is {round(weight/0.45)}")
