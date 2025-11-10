#remove intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.difference(set2)
print(set3)

"----"
inputset=set(map(int,input("enter the set elemements: ").split()))
print("your set is: ",inputset)
print("is it superset of itself?",inputset.issuperset(inputset))
set1={50,20}
set2={70,80}
print(inputset.issuperset(set1))
print(inputset.issuperset(set2))

set1={1,2,3,4,5}
print(len(set1))
for i in set1:
    check=int(input("enter a number"))
    if check in set1:
        print("present")
    else:
        print("not present")