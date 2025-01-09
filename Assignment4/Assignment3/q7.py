def add_lists(list1,list2,list3):
    return list(map(lambda x,y,z:x+y+z,list1,list2,list3))
print(add_lists ([1,2,3],[3,4,3],[6,2,3]))
#print(result)
print()

def sub_lists(list1,list2,list3):
    return list(map(lambda x,y,z:x-y-z,list1,list2,list3))
print(sub_lists ([1,2,3],[3,4,3],[6,2,3]))

def mul_lists(list1,list2,list3):
    return list(map(lambda x,y,z:x*y*z,list1,list2,list3))
print(mul_lists ([1,2,3],[3,4,3],[6,2,3]))