7num=int(input("Enter the number :"))
mylist=[1,2,3,4,5,6,7,8,9,10]
#print(mylist)
l2=[num*i for i in mylist]
print(f'THE TABLE OF ENTERED NUMBER  {num}:{l2}')

#print(l2)

'''
match num:
    case 1: l2=[num*i for i in mylist] 
    case 2: l2=[num*i for i in mylist] 
    case 3: l2=[num*i for i in mylist] 
    case 4: l2=[num*i for i in mylist] 
    case 5: l2=[num*i for i in mylist] 
    case 6: l2=[num*i for i in mylist] 
    case 7: l2=[num*i for i in mylist] 
    case 8: l2=[num*i for i in mylist] 
    case 9: l2=[num*i for i in mylist] 
    case 10: l2=[num*i for i in mylist]
print(l2) 
'''

'''
print(f'THE TABLE OF NUMBER {num}:')    
for i in range(1,11):
    print(num*i) 
'''   