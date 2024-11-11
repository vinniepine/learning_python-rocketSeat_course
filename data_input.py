# Data input
""" age = input("Quantos anos você tem?")
 
The input we'll get will be in the string format since 
comparisons can't be made between string types, we'll need to cast the input to 'int' type"""


# Casting user's string input into an 'int' type.
age = int(input("Quantos anos você tem?")) # this casting will assure we obtain a comparable value 
print("Exemplo de comando 'if':")
if age >= 18:
    print("Você é maior de idade.")
elif age >= 12:
    print("Você é adolescente.")
else:
    print("Você é menor de idade")

message = "Pode tirar a carteira de habilitação " if age >= 18 else "Você não pode tirar a carteira de habilitação"
print(message)
