# 'While' iterates through the code as long as the condition it is given is True
print("Exemplo de loop while")
counter = 0
while counter < 5:
    print("Contagem:", counter)
    counter += 1
print("Programa finalizado")

# the example above is the same as follows:
counter = 0
while True:
    print("Contagem:", counter)
    counter += 1
    if counter == 5:
        break

print("Programa finalizado")