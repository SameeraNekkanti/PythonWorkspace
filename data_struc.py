list1=[1,4,6,12,4,7]
set1={3,1,6,10,9}
a=[]  #give null set
for i in list1:
    for j in set1:
        if i==j:
            a.append(i)
print(a)


