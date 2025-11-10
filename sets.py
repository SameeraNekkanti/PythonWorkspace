
a={1,2,3,4,5,6}
b={3,4,5,6,7,8}
p=a.difference(b)
q=b.difference(a)
print("missing numbers are in set a: ",p)
print("missing numbers are in set b: ",q)
print()
a={1,2,3,4,5,6}
b={3,4,5,6,7,8}
p=set()
for i in a:
    if i not in b:
        p.add(i)
q=set()
for j in b:
    if j not in a:
        q.add(j)
print("missing numbers are in set a: ", p)
print("missing numbers are in set b: ", q)
 