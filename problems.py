#CHECK LEAP YEAR
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print("Leap year")
else:
 print("Not a leap year")

#CHECK TRAINGLE TYPR
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")

#GET SUM WITHIN A RANGE
sum=0
for i in range(1,51):
    sum+=i
print(sum)