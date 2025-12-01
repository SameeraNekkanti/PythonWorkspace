#4,5,6,8
#duplicate chars:
n=input("enter a string: ")
dupe=""
for i in n:
    if i not in dupe and n.count(i)>1:
       dupe+=i
print(",".join(dupe))

