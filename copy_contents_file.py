
f=open("superstar.txt","r")
q=open("sample.txt","w")
q.write(f.read())
f.close()
q.close()