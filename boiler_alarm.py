import time
low=0
high=0
while True:
    temp=float(input("enter temp in F"))
    burner=input("on or off").lower()
    interval=30
    if temp<140 and burner=="off":
        low+=interval
        high=0
        if low>=3: #5*60
            print("under heat alarm!!!")
    elif 140 <= temp <= 200 and burner == "off":
        low=0
        high=0
        print("normal")
    elif temp > 200 and burner == "on":
        high+=interval
        low=0
        if high>=6:
            print("over heat!!!")
    else:
        low=0
        high=0
        print("system functioning normally")
    time.sleep(5)
