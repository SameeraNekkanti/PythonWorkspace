#iterative
a=[101, 124, 139, 188, 203, 217, 245, 299]
e=int(input("enter the target value: "))
low=0
high=len(a)-1
p=-1
count=0
while low<=high:
    mid=int((low+high)/2)
    count+=1
    if a[mid]==e:
        p=mid
        break
    elif a[mid]<e:
        low=mid+1
    else:
        high=mid-1
print(p)
print(count)

#recursive
def binary_search(d,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if d[mid]==key:
        return mid
    elif d[mid]<key:
        return binary_search(d,mid+1,high,key)
    else:
        return binary_search(d,low,mid-1,key)

d=[2200, 2750, 3000, 3499, 4200, 5000, 5700]
print(binary_search(d,0,len(d)-1,2200))

def binary_search(array,target,low,high):
    while low<=high:
        mid=(low+high)//2
        if target==array[mid]:
            return mid
        elif array[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
result = binary_search(array, target, 0, 8)
print(result)