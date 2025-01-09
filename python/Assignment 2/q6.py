'''
def string_reversal():
    s=input("Enter a string: ")
    rs=s[::-1]
    return rs
if __name__=="__main__":
    print(string_reversal())
'''

def string_reversal():
    s=input("Enter a string: ")
    print(f"Original String:", s)
    reversed_s=''
    index=len(s)-1

    while index>=0:
        reversed_s+=s[index]
        index=index-1
    print(reversed_s)
string_reversal()







