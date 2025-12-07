
#multiplication table
limit=int(input("enter the limit"))
for i in range(limit):
    for j in range(10):
        print(i+1,"x",j+1,"=",(i+1)*(j+1))
        #for starts from 0