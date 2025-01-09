'''
def slicing():
    list1=[1,3,5,7,9,11,13,15,17,19]
    print(list1)
    list2=[] #list1[::2]
    list3=[]#list1[1::3]
    for index,value in enumerate(list1):
        if index %2==0:
           list2.append(index)
           list3.append(value)
    print(list2)
    print(list3)
'''
def slicing():
   #list1=[1,3,5,7,9,11,13,15,17,19]
    list1= [int(input(f"Enter element {i + 1}: ")) for i in range(10)]
    print(list1)
    list2=list1[1::2]
    print(list2)

if __name__=='__main__':
    slicing()
