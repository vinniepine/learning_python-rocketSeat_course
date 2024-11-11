# Creating a tuple as an example
my_tuple = (1, 2, 2, 7, 3, 4, 2)

print("Minha tupla:", my_tuple)
print("Minha tupla[0]:",my_tuple[0])
print("Minha tupla[1]:",my_tuple[1])
print("Minha tupla[2]:",my_tuple[2])
print("Minha tupla[-1]:",my_tuple[-1])


# count() method - it counts how many times a value appears
counting = my_tuple.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", counting)

index = my_tuple.index(3)
print("Índice da primeira ocorrência do elemento 3:", index)