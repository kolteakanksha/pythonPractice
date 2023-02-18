#number=[5,2,7,9]
#for freq in number:
 #   if number[0]>
  #  print('*' * freq)

#for count in range(0, 10):
  #  print(count)

lists = [2, 20, 90, 80]
thirdmax = lists[0]
length: int = len(lists)
position= 3-1
for num in lists:
    if num > thirdmax:
        thirdmax = num
        thirdmax = (position+thirdmax) % length
print(thirdmax.pop(lists))


