
#Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for item in list2:
    list1.append(item)      
print("Concatenated List:", list1)

# antother way to do it
#Using extend() method
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Concatenated List using extend():", list1)
