n=int(input("enter the no. of students"))
i=0
students=[]
while i<n:
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter total marks: "))
    students.append((roll,marks))
    i+=1

def bubble_sort(students):
    n=len(students)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if students[j][1] < students[j + 1][1]:
                swapped=True
                students[j], students[j + 1] = students[j + 1], students[j]
        if not swapped:
            break
bubble_sort(students)
print("\nSorted list:")
for i in students:
    print(i,end=" ")

def binary_search(low,high,key,students):
    if low > high:
        return -1

    mid=(low+high)//2
    if students[mid][0]==key:
        return mid
    elif students[mid][0]<key:
        return binary_search(mid+1,high,key,students)
    else:
        return binary_search(low,mid-1,key,students)
rollno=int(input("enter roll no. to search: "))
low=0
high=len(students)-1
pos = binary_search(low, high, rollno, students)
if pos!=-1:
    print("marks:",students[pos][1])
    print("Rank:",pos + 1)
else:
    print("Student not found")
