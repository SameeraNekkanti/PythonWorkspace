votes = {"Alice": 10, "Bob": 15, "Charlie": 7}

def voting_system():
    m=int(input("enter"))
    for i in range(m):
        n=input("enter user name")
        if n in votes:
            votes[n]+=1
        else:
            votes[n]=1
    return votes

print(voting_system())
print("final vote count")
winner=max(votes,key=votes.get)
print("winner:",winner)
