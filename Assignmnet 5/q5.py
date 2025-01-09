fp=open('input.txt','r')
content=fp.read()
reversed_content = content[::-1]
f=open('reversed.txt','w')
f.write(reversed_content)
print("content written sucessfuly")