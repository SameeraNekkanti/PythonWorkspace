# To implement basic arithmetic operations with a calculator interface.
count=0
number_of_runs = int(input("ENter the number of runs you want."))
while(count < number_of_runs):
    number_1 = int(input("Enter a number:"))
    number_2 = int(input("Enter a number:"))
    choice = input("Enter your choice (+ or - or * or /):")
    if(choice == "+"):
        print("You have chosen addition")
        result = number_1+number_2
        print(result)
    elif(choice == "-"):
        print("You have chosen substraction")
        result = number_1-number_2
        print(result)
    elif(choice == "*"):
        print("You have chosen multiplication")
        result = number_1*number_2
        print(result)
    elif(choice == "/"):
        print("You have chosen division")
        result = number_1/number_2
        print(result)   
    elif(choice == "0"):
        break
    count = count + 1
print("Program ends.")