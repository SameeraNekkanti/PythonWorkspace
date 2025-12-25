n=int(input("enter the number of contacts: "))
contact=[]
i=0
while i<n:
    name=input("enter the name")
    phone=int(input("enter the phone number"))
    contact.append((name,phone))
    i+=1
print(contact)
def selection(contact,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if contact[j]<contact[min]:
                min=j
        contact[i],contact[min]=contact[min],contact[i]
    return contact
size=len(contact)
print(selection(contact,size))

def binarysearch(contact,low,high,nam):
    if low>high:
        return -1
    mid=(low+high)//2
    if contact[mid][0]==nam:
        return mid
    elif contact[mid][0]<nam:
        return binarysearch(contact,mid+1,high,nam)
    else:
        return binarysearch(contact,low,mid-1,nam)
nam=input("enter the name to search: ")
low=0
high=len(contact)-1
pos=binarysearch(contact,low,high,nam)
if pos==-1:
    print("contact not found")
else:
    print("contact found",contact[pos])
