def multiply(a,*args):
    for i in args:
        print(a*i)
if __name__=="__main__":
    (multiply(4,3,4,7,9,12,20))