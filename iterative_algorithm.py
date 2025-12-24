def myfunc():
    global x
    x="chinni"
myfunc()
print("bad girl is: "+x)

q=3
i=567
p=49.95
o="pay{2} dollars for {0} pieces of item {1}"
print(o.format(q,i,p))
n=6
i=1
count=1
while count<=n:
    i=i*count
    count+=1
print(i)

#bubble sort
arr=[3,5,3,2]
n=len(arr)
for i in range(0,n-1):
    swapped=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped=True

    if not swapped:
        break
print(arr)

#imperitive programming
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
n=6
print(fact(n))