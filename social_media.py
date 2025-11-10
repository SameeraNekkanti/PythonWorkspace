insta={'sami','chinni','hasini'}
twitter={'sreeja','pranavi','sami'}
print("both: ")
for i in insta:
    for j in twitter:
        if i==j:
            print(i)
print()

instaonly=insta.difference(twitter)

print("only insta",instaonly)

print()

twitteronly=twitter.difference(insta)
print("only on twitter: ",twitteronly)

r=set(insta|twitter)
print(r)
a=instaonly|twitteronly
print(a)