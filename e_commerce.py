n=int(input("enter no. of products"))
i=0
prices=[]
while i<n:
    price=float(input("enter the price of the item: "))
    prices.append(price)
    i+=1
print(prices)
def insertion(prices):
    n=len(prices)
    if n<=1:
        return prices
    for i in range(1,n):
        key=prices[i]
        j=i-1
        while j>=0 and key<prices[j]:
            prices[j+1]=prices[j]
            j-=1
        prices[j+1]=key
    return prices
insertion(prices)
print("\nSorted book list:")
for i in prices:
    print(i,end=",")

def binarysearch(prices,low,high,budget):
    if low>high:
        return -1
    mid=(low+high)//2
    if prices[mid]==budget:
        return mid
    elif prices[mid]<budget:
        return binarysearch(prices,mid+1,high,budget)
    else:
        return binarysearch(prices,low,mid-1,budget)
budget=float(input("enter the budget: "))
low=0
high=len(prices)-1
pos=binarysearch(prices,low,high,budget)
if pos!=-1 and prices[pos]==budget:
    print("Exact match found:", prices[pos])
elif pos >= 0:
    print("Nearest cheaper price:", prices[pos])
else:
    print("No product within budget")