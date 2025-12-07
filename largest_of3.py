#Selection Algorithm (Find largest of three numbers)
x=int(input("enter the number x: "))
y=int(input("enter the number y: "))
z=int(input("enter the number z: "))
if x>y and x>z:
    print("x is greatest")
elif y>z:
    print("y is greatest")
else:
    print("z is greatest")
    