dic1={
    "ria": 788,
    "sia":898
}
print(dic1)

dic2={
    "riya": 78,
    "sia":89,
    "riy": 780,
    "si":890,
    "dic3":{
    "r": 78,
    "s":89},
    "dic4":{
        9:89,
        98:00
    }
}

print(dic2)
dic1.update(dic2)
print(dic1)
print(dic1.values())
print(dic1.keys())
print(dic1["ria"])
