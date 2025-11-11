words=['red','green','red','blue','red','red','green']
a=set(words)
print(a)
red=0
green=0
blue=0
for i in words:
    if i=='red':
        red+=1

    if i=='blue':
        blue+=1

    if i=='green':
        green+=1
    
print(red,green,blue)