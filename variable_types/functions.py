# Example
def greeting(name):
    print(f"Olá, {name}!")

print("\nChamando a função 'greeting':")
greeting("Vinnie")
greeting("Oliver")

# Functions with a return
def square(number):
    result = number ** 2 
    return result
print("\nChamando a função 'square:")
print(square(5))

# Function with multiple parameters
def sum(number1, number2):
    return number1 + number2

print("\nChamando a função soma:")
sum_result = sum(20, 50)
print("20 + 50: %s" % sum_result)
