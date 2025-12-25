import array as arr

def add_reading(temparr,timestamp,temp,date,time):
    temparr.append(temp)
    timestamp.append((date,time))
def update_sensors(id,newid):
    if newid not in id:
        id.add(newid)
    return id
def compute_avg(temparr,avgdict,id):
    if len(temparr) == 0:
        print("No readings available.")
        return avgdict
    total=0
    for i in temparr:
        total+=i
    avg=total/len(temparr)
    avgdict[id]=avg
    return avgdict
temparr=arr.array('f')
timestamp=[]
id=set()
avgdict={}
while True:
    print("\n--- Temperature Sensor Analyzer ---")
    print("1. Add temperature reading")
    print("2. Add sensor ID")
    print("3. Compute average temperature for a sensor")
    print("4. Exit")
    choice =input("Enter your choice: ")
    if choice == "1":
        temp = float(input("Enter temperature: "))
        date = input("Enter date (DD-MM-YY): ")
        time = input("Enter time (HH:MM): ")
        add_reading(temparr,timestamp,temp,date,time)
        print("Reading added successfully.")

    elif choice == "2":
        newid = input("Enter sensor ID: ")
        update_sensors(id, newid)
        print("Sensor ID added.")
    elif choice == "3":
        id = input("Enter sensor ID to store average: ")
        compute_avg(temparr, avgdict, id)
        print("Average calculated.")
    elif choice == "4":
        print("\nFinal Data:")
        print("Temperatures:", list(temparr))
        print("Timestamps:", timestamp)
        print("Sensor IDs:", id)
        print("Averages:", avgdict)
        break

    else:
        print("Invalid choice. Try again.")