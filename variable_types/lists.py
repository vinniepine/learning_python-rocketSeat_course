# Declaring the list
my_list = [1, 2, 3, 4, 5, "rocketSeat", True, False]

# Showing the list
print("My List", my_list)

# Showing the list at an index
print("My list [0]:", my_list[0])
print("My list [0]:", my_list[5])

# Slicing (fatiamento)
my_list[0] = "python"
print("My list [1:8]:", my_list[1:8])
print(my_list[:6]) # the same as print(my_list[0:6]);
print(my_list[2:]) # it prints all the elements of the list from index 2 on;

# append() method: it adds an element to the end of the list
my_list.append(6)
print("Após o append(6):", my_list)

# index() method
newIndex = my_list.index(6)
print("Índice do elemento 6:", newIndex)

# insert() method - it inserts an element into a specific index
my_list.insert(2, "inserção") # the index at which something is inserted is followed by the insertion
print("Após a 'insertion':", my_list) 

# pop() method - it removes an item at a given index of the list
removed_element = my_list.pop(3)
print("Após pop(3):", my_list)
print("Elemento removido:", removed_element)

# remove() method - it removes the first element on the list with the specified value
print("Antes de remove(True):", my_list)
my_list.remove(True)
print("Após remove(True):", my_list)
