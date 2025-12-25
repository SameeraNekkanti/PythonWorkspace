n=int(input("enter no. of buses: "))
i=0
departure=[]
while i<n:
    times=input("enter the timings of buses: ")
    departure.append(times)
    i+=1
print(departure)
def insertionsort(departure):
    n=len(departure)
    if n<=1:
        return departure
    for i in range(1,n):
        key=departure[i]
        j=i-1
        while j>=0 and key<departure[j]:
            departure[j+1]=departure[j]
            j-=1
            departure[j+1]=key
    return departure
insertionsort(departure)
print("\nSorted book list:")
for i in departure:
    print(i,end=",")
def binarysearch(departure,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if departure[mid]==target:
        return mid
    elif departure[mid]<target:
        return binarysearch(departure,mid+1,high,target)
    else:
        return binarysearch(departure,low,mid-1,target)
target=input("enter the time: ")
low=0
high=len(departure)-1
pos=binarysearch(departure,low,high,target)
if pos!=len(departure) and departure[pos] == target:
    print("Bus available at", times[pos])
else:
    print("No bus at this time")
    if pos < len(departure):
        print("Next bus at", departure[pos])
    else:
        print("No later buses today")