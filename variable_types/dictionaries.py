# Dictionaries are collections of non-orderes pairs of a key and a value

# Creating a dictionary as an example
person = {"name": "Vinnie", "age": 30, "city": "X-Waters"}
print("Meu dicionário de exemplo", person)

# Accessing values by the key
print("Nome:", person["name"])
print("Idade:", person["age"])
print("Cidade:", person["city"])

# Adding a key with a value
person["surname"] = "Pine"
print("Surname:", person["surname"])

# Updating or changing an existing value

person["age"] = 31
print("Idade atualizada:", person["age"])

# Removing a key-value pair
del person["surname"]
print("Meu dicionário de exemplo:", person)

# Methods: keys(), values(), items()
# keys() method
keys = person.keys()
print("Chaves do dicionário:", keys)

# Accessing each element of the dictionary by casting it into a list
keys = list(person.keys())
print("Primeira chave:", keys[0])

# values() method
values = list(person.values())
print("Valores do dicionário", values)
print("Primeiro valor:", values[0])

# items() method 
## instead of getting a list with simple values, 
## we get a list in which every element is a tuple with a key-value pair 
items = person.items()
print("Pares chave-valor do dicionário:", items)
print("Primeira chave-valor: %s = %s" % (items[0][0], items[0][1]))
