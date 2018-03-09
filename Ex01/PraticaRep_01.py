def ePar(n):
    return n % 2 == 0


a = int(input("Digite um número inteiro: "))
while (a != 0):
    if ePar(a):
        print("%d é Par" % a)
    else:
        print("%d é Impar" % a)

    a = int(input("Digite um número inteiro: "))
