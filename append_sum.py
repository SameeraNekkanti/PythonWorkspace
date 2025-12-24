f=open("sample.txt","r")

total=0
for i in f:
    num=i.strip()
    if num.isdigit():
        total+=int(num)
print(total)
f.close()
f=open("sample.txt","a")
f.write("\n"+str(total))
f.close()
