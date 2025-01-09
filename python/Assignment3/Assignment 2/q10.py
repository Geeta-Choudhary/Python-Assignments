list1=[int(input(f"enter the element {i+1}:")) for i in range(10)]
#list1=[1,2,3,4,5,6,7,8,9,10]
#list2=[11,12,13,14]
print(list1)
list1.append(11)
print(f"Appending the element at end :{list1}")
list1.pop(0)
print(f"After removing the element{list1}")

print(f"Deleting a particular element the deleted element:{list1.pop(2)}")

list1.insert(3,60)
print(f"Inserting at particular index :{list1}")

print(f"Sorting in ascending order :{sorted(list1)}")
print(f"Sorting in descending order :{sorted(list1, reverse=True)}")


