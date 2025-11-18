text = "hello world"
def frequency():
    freq={}
    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
print(frequency())