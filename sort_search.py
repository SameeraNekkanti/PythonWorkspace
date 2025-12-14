def bubble(rolls, marks):
    for i in range(len(rolls)):
        for j in range(len(rolls)-i-1):
            if marks[j] < marks[j+1]:
                t = marks[j]
                marks[j] = marks[j+1]
                marks[j+1] = t

                t = rolls[j]
                rolls[j] = rolls[j+1]
                rolls[j+1] = t

def binary_search(rolls, marks, roll):
    l = 0;
    h = len(rolls)
    
    t = marks[rolls.index(roll)]

    while(l <= h):
        mid = (l+h)//2

        if marks[mid] == t:
            return mid+1
        elif marks[mid] < t:
            h = mid-1
        else:
            l = mid + 1
    return -1
        
N = int(input("Enter the number of Students"))

rolls = []
marks = []
for i in range(N):
    r = int(input(f"Enter the roll number for studet {i+1}"))
    tm = int(input(f"Enter the total marks of student {i+1}"))
    rolls.append(r)
    marks.append(tm)

bubble(rolls, marks)

r = int(input("Enter a roll number"))
rank = binary_search(rolls, marks, r)

if rank != -1:
    print("The rank and marks obtained are", rank, marks[rank-1])
else:
    print("Roll number not found")