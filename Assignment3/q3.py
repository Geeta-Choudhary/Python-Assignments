list1=["Apple","banana","ant","Cherry","Alphonsa"]
print(list1)
print()
ans1=[item[0].lower()=='a'for item in list1]
print(ans1)
print()
ans=filter(lambda item:item[0].lower()=='a',list1)
print(list(ans))
print()
ans1 = [
    f"{item} starts with A" if item[0].lower() == 'a' else f"{item} does not start with A"
    for item in list1
]
for result in ans1:
    print(result)



print()
st=(lambda s:s[0].lower()=='a')('Mango')
print(st)