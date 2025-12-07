def longest_line():
    longest=""
    with open("sample.txt","r") as f:
        for i in f:
            i=i.strip()
            if len(i)>len(longest):
                longest=i
    return longest
print(longest_line())
