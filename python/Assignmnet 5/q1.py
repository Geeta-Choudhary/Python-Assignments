list1=[i*i for i in range(1,21)]
print(f"The  list of the squares of all numbers from 1 to 20.\n{list1}")

list2=[i*i for i in range(1,21) if i%2 == 0 ]
print(f"The  list of the squares of all"
      f" numbers from 1 to 20.\n{list2}")