#forbidden characters
forbidden_chars = {' ', '!', '@', '#', '$', '%', '^', '&', '*'}
password=input('enter your password: ')
total=0
set1=set()
for i in password:
    if i in forbidden_chars:
        total+=1
        set1.add(i)
print(set1)
print(total)