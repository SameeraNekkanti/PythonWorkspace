#sum of elements
import array as arr
a=arr.array('i',[1,2,3,4])
count=0
for i in a:
    count+=i
print("sum of numbers in the array is: ",count)

#largest, smallest
arr=[12,45,3,4,6,32]
smallest=arr[0] #assume
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest,smallest)

#even,odd
arr=[1,2,3,4,5,6,7]
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("total even numbers:",even)
print("total odd: ",odd)

