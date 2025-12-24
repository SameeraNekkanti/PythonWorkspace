r = [1101, 1120, 1155, 1180, 1250, 1302, 1420, 1501]
e=int(input("enter the target value: "))
low=0
high=len(r)-1
p=-1
count=0
while low<=high:
    mid=int((low+high)/2)
    count+=1
    if r[mid]==e:
        p=mid
        break
    elif r[mid]<e:
        low=mid+1
    else:
        high=mid-1
print(p)
print(count)