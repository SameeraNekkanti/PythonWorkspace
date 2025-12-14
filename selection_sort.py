def sel_sort(l):
    n=len(l)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if (l[j]<l[mini]):
                mini=j
            l[i],l[mini]=l[mini],l[i]
    return l
e = [2,9,4,9,6]
print(sel_sort(e))
