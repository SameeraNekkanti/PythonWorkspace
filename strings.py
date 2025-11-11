text=input("Enter a string: ")
print(text)


i="A12B34"
count=0
for ch in i:
    if ch.isdigit():
        count+=1
print(count)

i="hello"
if i.isalpha():
    print("it is a string")
else:
    print("no")

print("---"*9)
l="My name   is ABC"
space=l.count(' ')
print(space)

print("---"*40)
text = input("Enter a string: ")
char=input("Enter a string: ")
print(text.index(char)+1)

text=input("Enter a string: ")
if (text==text[::-1]):
    print("yes")
else:
    print("no")

print(":"*40)
text=input("Enter a string: ")
count=0
for ch in text:
    if(ch.isdigit()):
        count+=int(ch)
print(count)

print(":"*40)
text=input("Enter a string: ")
h=text.replace("!@#$%^&*?/\|","")
print(h)