#linear search
'''a=[57, 12, 89, 33, 71, 46, 20, 95]
p=-1
e=33
i=0
while i<len(a):
    if a[i]==e:
        p=i
        break
    i+=1 
print(p)'''

#recursive linear search
b=[14, 27, 39, 41, 56, 72]
def linear_search(b,key,i):
    if i>len(b): #base case
        return -1
    if b[i]==key:
        return i
    return linear_search(b,key,i+1)

print(linear_search(b,41,0))