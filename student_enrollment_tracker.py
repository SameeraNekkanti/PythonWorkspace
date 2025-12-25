
def add_student(name_list,student_tuple,status_dict):
    name=input("enter student name: ").strip()
    year=int(input("enter enrollment year: "))
    name_list.append(name)
    student_tuple.append((name,year))
    status_dict[name]="Active"
    print("student added succesfully!")

def update_activities(actset):
    actset={"cricket","football"}
    newact=input("enter the activity")
    if newact not in actset:
        print("activity added!!!")
        actset.add(newact)
    else:
        print("Activity already exists!")

def check_membership(statusdict,name):
    if name in statusdict:
        status=statusdict[name]
    else:
        status="not found"
    active=0
    for i in statusdict.values():
        if i=="Active":
            active+=1
    return(status,active)
print("=== Student Enrollment Tracker ===\n")
 
 # Initialize collections
name_list = []
student_tuples = []
actset = set()
status_dict = {
    "Bob": "Active",
    "Sam": "Inactive"
}

 
while True:
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Add Activity")
    print("3. Check Membership")
    print("4. Display All Data")
    print("5. Exit")
 
    choice = input("\nEnter your choice (1-5): ").strip()
 
    if choice == '1':
        
        add_student(name_list, student_tuples, status_dict)
 
    elif choice == '2':
        update_activities(actset)
 
    elif choice == '3':
        name = input("Enter student name to check: ").strip()
        status, active_count = check_membership(status_dict, name)
        print(f"Status: {status} | Total Active Members: {active_count}")
 
    elif choice == '4':
        print("\n--- Current Data ---")
        print(f"Names List: {name_list}")
        print(f"Students (Tuples): {student_tuples}")
        print(f"Activities (Set): {actset}")
        print(f"Statuses (Dict): {status_dict}")
 
    elif choice == '5':
        print("Thank you! Exiting...")
        break
 
    else:
        print("Invalid choice! Please try again.")
