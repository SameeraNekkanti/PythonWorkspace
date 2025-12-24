day=input("season(cold or snowing or both?): ")
if day=="both":
    print("outfit: parka")
elif day=="cold":
    print("outfit: jacket")
elif day!="cold":
    print("outfit: formal")
else:
    print("try again")