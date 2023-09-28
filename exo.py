D = {"name": "Mahandry", "Age": 36}

nam = D["name"]
ag = D["Age"]
L = D.values()
print(D)
print(f"{nam}, {ag}")
print(L)

d = {"mercure": 1, "venus": 2, "terre":3, "mars":4}
for planet in d.keys():
    print(planet)
for num in d.values():
    print(num)

tuple_of_dictionaries = (
    {"name": "John Doe", "age": 30},
    {"name": "Jane Doe", "age": 25},
    {"name": "Peter Smith", "age": 40},
)

print(tuple_of_dictionaries)
# (('John Doe', 30), ('Jane Doe', 25), ('Peter Smith', 40))
print(tuple_of_dictionaries[1])
name = tuple_of_dictionaries[0]["name"]
age = tuple_of_dictionaries[0]["age"]
print(name, age)
print(tuple_of_dictionaries[2]["name"], tuple_of_dictionaries[2]["age"])

for i in range(0, len(tuple_of_dictionaries)):
    print(tuple_of_dictionaries[i]["name"], tuple_of_dictionaries[i]["age"])

for i, dictionary in enumerate(tuple_of_dictionaries):
    print(dictionary["name"], dictionary["age"])