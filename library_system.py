n=int(input("enter no. of books"))
i=0
library=[]
while i<n:
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library.append((title, author))
    i += 1

def ss(library):
    n=len(library)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if library[j][0]<library[min][0]:
                min=j
        library[i], library[min] = library[min], library[i]
ss(library)
print("\nSorted book list:")
for i in library:
    print(i)
def binarysearch(low,high,title,library):
    if low>high:
        return -1
    mid=(low+high)//2
    if library[mid][0]==title:
        return mid
    elif library[mid][0]<title:
        return binarysearch(mid+1,high,title,library)
    else:
        return binarysearch(low,mid-1,title,library)
low=0
high=len(library)-1
title=input("enter book title")
pos=binarysearch(low,high,title,library)
if pos!=-1:
    print("title:",library[pos][0])
    print("author: ",library[pos][1])
