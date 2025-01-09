def greet(name,msg="HELLo"):
    return name ,msg
if __name__=="__main__":
    print(greet(name='geeta',msg="GOOD morning"))
    print(greet("Indresh" ))
    print(greet(msg="GOOD morning" , name='geeta'))