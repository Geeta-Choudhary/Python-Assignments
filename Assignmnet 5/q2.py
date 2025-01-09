fruits={'orange':1,'banana':2,'apple':3}
print(fruits)
fruits=sorted(fruits.items(),key=lambda x:x[1],reverse=True)
print(fruits)
print()
inputs=[('apple', 3), ('banana', 2), ('orange', 1)]
print(inputs)
inputs=sorted(inputs,key=lambda item :item[1])
print(inputs)