
def merge_dict(d1,d2):
    for i in d1:
        for j in d2:
            if i==j:
                add= d1[i]+d2[i]
                d1[i]=add
                print(d1)
            else:
                {**d1, **d2}
                print(d1)


d1={"a":1,"b":2}
d2={"b":4,"c":3}
d3={}
merge_dict(d1,d2)