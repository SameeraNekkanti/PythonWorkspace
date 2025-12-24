f=open("sample.txt","r")
sub={'1':"!"}
en=open("even.txt","w")
for i in f:
    new=""
    for ch in i:
        if ch in sub:
            new+=sub[ch]
        else:
            new+=ch
    en.write(new)

f.close()
en.close()