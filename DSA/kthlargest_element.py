n=int(input("enter number of elements: "))
nums=list(map(int, input("enter elements: ").split()))
k=int(input("enter k: "))

for i in range(k):
    max_index=i
    for j in range(i+1,n):
        if nums[j]>nums[max_index]:
            max_index=j

    nums[i], nums[max_index]=nums[max_index],nums[i]
print(f"{k}th largest element=", nums[k-1])