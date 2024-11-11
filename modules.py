# Modules are archives that contain instructions and definitions that may be reused by other programs
print("Exemplo de importação de um módulo padrão")
from math import sqrt
root = sqrt(25)
print(f"A raiz quadrada de 25 é:", root)
""" 
poderíamos importar todo o módulo math (import math) e usar o método math.sqrt()
contudo, isso faz pesar a biblioteca 
"""

# Importando o meu módulo
from my_module import greeting, double
greeting("Vinnie")
doubled = double(6)
print("O dobro de 6 é %s" %doubled)