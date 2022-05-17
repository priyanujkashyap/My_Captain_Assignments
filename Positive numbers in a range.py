list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
list3=[]
list4=[]
for num in list1:
    if num > 0:
       list3.append(num)
print(*list3, sep=",")
for num in list2:
    if num > 0:
        list4.append(num)
print(list4)     
