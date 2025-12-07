def word_lines(word):
    count=0
    f=open("word_freq.txt","r")
    for i in f:
        if word.lower() in i.lower():
            count+=1
    f.close()
    return count
wordtarg = input("Enter the word to search for: ")  
print(word_lines(wordtarg))
