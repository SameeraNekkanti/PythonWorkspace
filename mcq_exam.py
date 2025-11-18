correct="ABCDABCD"
n=int(input("enter the number of students"))
score=[]
count=0
while (count<n):
    opt=input("enter your options").strip()
    m=0
    for i in range (len(correct)):
        if opt[i]==correct[i]:
            m+=1
    score.append(m)
    count+=1
print(score)