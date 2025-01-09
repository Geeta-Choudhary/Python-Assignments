def sum_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result

print(sum_numbers(1,2,3,4,5))
print(sum_numbers(0,2))
print(sum_numbers(3,4))
print(sum_numbers(1))