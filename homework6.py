my_dict={"Vasya":1979,"Egor":1999,"Masha":2002}
print("Dict:",my_dict)
print("Existing value:",my_dict["Egor"])
print("Not existing value:",my_dict.get("Denis"))
my_dict.update({"Kamila":1981,"Artem":1915})
print("Deleted value:",my_dict["Egor"])
del my_dict["Egor"]
print("Modified dictionary:",my_dict)
print(" ")
my_set={1,"Яблоко",42.314,1,1,1,"Яблоко"}
print("Set:",my_set)
my_set.update((13,(5,6,1.6)))
my_set.remove(1)
print("Modified set:",my_set)