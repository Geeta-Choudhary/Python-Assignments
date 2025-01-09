'''
def rounding_off():
    list1=[1.2,2.5,3.8]
    list2=[]
    for i in list1:
        list2.append(round(i))
    print(list2)

if __name__=="__main__":
    rounding_off()
'''

def rounding_off(numbers):
    rounded_numbers = [int(i + 0.5) if i % 1 >= 0.5 else int(i) for i in numbers]
    print(rounded_numbers)

# Example usage
rounding_off([1.2, 2.5, 3.8])





