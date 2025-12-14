#to calculate factorial
def factr(n):
    if n==1:
        return 1
    else:
        return n*factr(n-1)
print("factorial is",factr(5))

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact(9))
