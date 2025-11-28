#to add first n numbers:
'''n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=i
print(i)'''

#multiplication table:
'''n=int(input("enter the end limit"))
for i in range(n):
    for j in range(10):
        print(i+1,"*",j+1,"=",(i+1)*(j+1))'''

#count the vowels:
word=input("enter the string").lower()
vowels=["a","e","i","o","u"]
count=0
for i in word:
    if i in vowels:
        print(i,"is vowel")
        count+=1
    else:
        print(i,"not vowel")
print("no. of vowels",count)
