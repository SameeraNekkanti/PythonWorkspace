f=open("sample.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
for i in f:
    m=i.strip()
    if m.isdigit():
        m=int(i)

        if m%2==0:
            even.write(i+"\n")
        else:
            odd.write(i+"\n")

f.close()
even.close()
odd.close()