f=open("superstar.txt")
freq={}
for i in f:
    words=i.split()
    for j in words:
        if j in freq:
            freq[j]+=1
        else:
            freq[j]=1
f.close()
f=open("superstar.txt","a")
f.write("\n"+str(freq))
print(freq)
f.close()