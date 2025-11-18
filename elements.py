elements = {
    "H":  {"name": "Hydrogen",  "Z": 1,  "mp": 14,   "bp": 20},
    "He": {"name": "Helium",    "Z": 2,  "mp": 1,    "bp": 4},
    "Li": {"name": "Lithium",   "Z": 3,  "mp": 453,  "bp": 1603},
    "Be": {"name": "Beryllium", "Z": 4,  "mp": 1560, "bp": 2742},
    "B":  {"name": "Boron",     "Z": 5,  "mp": 2349, "bp": 4200},
    "C":  {"name": "Carbon",    "Z": 6,  "mp": 3915, "bp": 3915},
    "N":  {"name": "Nitrogen",  "Z": 7,  "mp": 63,   "bp": 77},
    "O":  {"name": "Oxygen",    "Z": 8,  "mp": 54,   "bp": 90},
    "F":  {"name": "Fluorine",  "Z": 9,  "mp": 53,   "bp": 85},
    "Ne": {"name": "Neon",      "Z": 10, "mp": 25,   "bp": 27}
}
total=0
total2=0
for i in elements:
    total+=elements[i]["mp"]
    for j in elements:
        total2+=elements[i]["bp"]

print(total)
print(total2)
def state(temp,symbol):
    data=elements[symbol] #access dict
    mp=data["mp"]
    bp=data["bp"]
    
    if temp<mp:
        return f"solid at {temp}k"
    elif  mp <= temp < bp:
        return f"liquid at {temp} K."
    else:
        return f" gas at {temp }k"
    
print(state(70, "O"))
print(state(500, "Li"))