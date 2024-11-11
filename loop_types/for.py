# For loop
"""
    It is used to iterate through a sequence of elements. It repeats 
    the same action for each element in the sequence. The structures 
    we've learned that have a sequence are: lists, tuples, dictionaries
"""

print("\nFor utilizando lista")
new_list = [ 1, 2, 3, 4, 5]
for ele in new_list:
    print(ele)

print("\nFor utilizando tupla")
new_tuple = (1, 2, 3, 4, 5,)
for ele in new_tuple:
    print(ele)

person = {"name": "Vinnie", "age": 30, "city": "X-Waters"}
print("\nFor utilizando dicionário - chaves")
for key in person.keys():
    print(key)

print("\nFor utilizando dicionário - chaves")
for value in person.values():
    print(value)

# we can declare two variables at the same time
print("\nFor utilizando dicionário - itens")
for key, value in person.items():
    print(f"{key}: {value}")

# Using 'for loop' with the range() function
# range(): returns a numeric interval in a list
print("Utilizando a função range()")
for number in range(0, 4): # == range(4)
    print("Número:", number)

# len()
print("Utilizando a função range() com len()")
range_list = [1, 2, 3, 4, 5]
print(range_list)
for index in range(0, len(range_list)):
    if index == 3:
        range_list[index] = 5
print(range_list) # mostra lista alterada no índice '3'

# enumarate() - mostra os dados de uma lista junto do índice em que elas estão de forma enumerada
enumarate_list = ["a", "b","c"]
for index, value in enumerate(enumarate_list):
    print(f"{index}: {value}")
    if index == 1:
        print("Índice 1")