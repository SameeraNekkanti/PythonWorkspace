products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
]
#bubble sort

def bubble_sort(products, key):
    n=len(products)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if products[j][key] > products[j + 1][key]:
                swapped=True
                products[j],products[j+1]=products[j+1],products[j]
        if not swapped:
            return
price_sorted = products.copy()
stock_sorted = products.copy()
name_sorted = products.copy()
id_sorted=products.copy()
bubble_sort(price_sorted, "price")
bubble_sort(stock_sorted, "stock")
bubble_sort(name_sorted, "name")
bubble_sort(id_sorted, "id")

print("Sorted by price:")
for p in price_sorted:
    print(p)

print("\nSorted by stock:")
for p in stock_sorted:
    print(p)

print("\nSorted by name:")
for p in name_sorted:
    print(p)


print("\nSorted by id:")
for p in id_sorted:
    print(p)

#binary search

def binary_search(products,id):
    first=0
    last=len(products)-1
    while first<=last:
        mid=(first+last)//2
        if products[mid]["id"]==id:
            return products[mid]
        elif products[mid]["id"] < id:
            first=mid+1
        else:
            last=mid-1
    return None

id=int(input("enter id to be searched: "))
r=binary_search(id_sorted,id)
for key,value in r.items():
    print(f"{key}: {value}")

print()

#linear search
def linear_search_by_name(products, name):
    result = []
    for i in range(len(products)):
        if name.lower() in products[i]["name"].lower():
            result.append(products[i])
            return result
    return None
name = "laptop"
f=linear_search_by_name(products, name)

for p in f:
    print(p)

def search_by_price(products,minp,maxp):
    result=[]
    for i in range(len(products)):
        if minp<=products[i]["price"]<=maxp:
            result.append(products[i])
    return result

minp = int(input("Enter minimum price: "))
maxp = int(input("Enter maximum price: "))

found = search_by_price(products, minp, maxp)

for p in products:
        for key, value in p.items():
            print(f"{key}: {value}")
        print()
