#number of times a number is present in a list
list2=[1,2,3,4,6]
list2.reverse()
print(list2)

list1=list(map(int,input("enter the list elemements: ").split()))
k=int(input("enter a number: "))
count=0

for i in list1:
    if i==k:
        count+=1
if count>0:
        print("it is present these many timez",count)
else:
       print("it is not present")