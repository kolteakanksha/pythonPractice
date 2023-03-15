name = input("> ").replace(" ", "").lower()

if name == name[::-1]:
    print(" It is a Palindrome")
else:
    print(" It is not a Palindrome")

# name= 'akanksha'# slicing
# print(name[1:-2])