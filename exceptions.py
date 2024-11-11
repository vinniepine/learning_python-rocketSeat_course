print("Exemplo de captura de exceções")
while True:
    try:
        number = int(input("Digite um número inteiro: "))
        resultado = 10 / number
    except ValueError as v:
        print(f"Value error: {v}")
        raise ValueError("Tipo de variáveis incompatíveis")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(resultado)
    finally:
        print("Operação finalizada")


