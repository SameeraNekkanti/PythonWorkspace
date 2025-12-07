#Printing current and previous number and their sum in a range(10)
prev=0
for i in range(1, 11):
     x_sum = prev + i
     print("Current Number", i, "Previous Number ", prev, " Sum: ", x_sum)
     prev=i
