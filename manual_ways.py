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

#reverse a string:
word=input("enter the word to be reversed: ")
rev=""
for i in range(len(word)):
    rev=word[i]+rev
print(rev) 