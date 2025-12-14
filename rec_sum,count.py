def recursive_sum(L):
    if L==[]:
        return 0
    else:
        return L[0]+recursive_sum(L[1:])
print("the sum is:",recursive_sum([1,2,3]))

def count_digits(n):
    if n<10:
        return 1
    else:
        return 1+count_digits(n//10)
print(count_digits(12345))  


    