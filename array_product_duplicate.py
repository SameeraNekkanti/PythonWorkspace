#max product
arr=[1,2,3,4,5,9]
max=arr[0]*arr[1]
pair=(arr[0],arr[1])
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        produc=arr[i]*arr[j]
        if produc>max:
            max=produc
            pair=(arr[i],arr[j])
print("highest is," , pair)
print("product is ", max)       

#duplicates removal
arr=[1,2,3,3,4,7,5,7]
new=[]
for i in arr:
    for j in i:
        if i!=j:
            new.append(i)
print("new array: ",new)

#reverse
arr=[1,2,3,4,5,6]
new=[]
for i in range(len(arr)):
    new.append(arr[-(i+1)]) #negative indexing
print(new)

    
