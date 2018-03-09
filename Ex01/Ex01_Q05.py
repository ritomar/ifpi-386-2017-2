def ePar(n):
    return n % 2 == 0

# Try ... except protege o código de entrada inválida.
try: 
    a = int(input("Digite um número: "))

    if ePar(a):
        print("Número Par")
    else:
        print("Número Impar")
except:
    print("Você não digitou um número válido.")



