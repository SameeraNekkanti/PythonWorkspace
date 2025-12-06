def writedata():
    n = int(input("Enter the number of students: "))
    record={}
    for i in range(n):
        name=input("Enter student name: ")
        score = int(input(f"Enter score for {name}: "))
        record[name] = score
    with open("student1.txt","w") as f:
        for name, score in record.items():
            f.write(f"{name},{score}\n")
print("done")
writedata()
