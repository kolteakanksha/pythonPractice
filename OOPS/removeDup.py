mylist = ["a", "b", "a", "c", "c"]
unique = []

for char in mylist:
    if char not in unique:
        unique.append(char)

print(unique)