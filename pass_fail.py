#Selection Algorithm (Decide Student Result: Pass or Fail)
marks=int(input("enter the marks of the student: "))
pass_marks=int(input("enter the passing mark: "))
if marks>=pass_marks:
    print("pass")
else:
    print("fail")

result=1
count=1
n=int(input('enter n'))
while count<=n:
    result=result*count
    count=count+1
print(result)