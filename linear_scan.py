#find largest number:
'''n=list(map(int,input("enter the list elements: )))
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)'''

#factorial calculation:
n=int(input("enter n value: "))
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(n))  

