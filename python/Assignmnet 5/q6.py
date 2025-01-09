source_filename=input("Enter a Source file name: ")
destination_filename=input("Enter a destination filename: ")
fp=open(source_filename,"r")
content=fp.read()
f=open(destination_filename,'w')
f.write(content)

print("Contented copied Successfully")
