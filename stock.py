list1=[1,2,3,4,5]
stock=[1,4,5,9,7]
print("the following orders can be fulfilled: ")
for i in list1:
    if i in stock:
        print(i,end=" ")
print("\nnot in stock: ")
for j in list1:
            if j not in stock:
                print(j,end=" ")
print("\nnew list of fulfillable order ids: ")
listnew=[]
for k in list1:
      if k in stock:
            listnew.append(k)
print(listnew)