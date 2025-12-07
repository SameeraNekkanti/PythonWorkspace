f=open("sample.txt","r")
q=open("mega.txt","r")
diff=[]
line=1
for line1, line2 in (f,q):
    if line1!=line2:
        diff.append(line)
    line+=1

f.close()
q.close()
print("Lines with differences:", diff)
    
