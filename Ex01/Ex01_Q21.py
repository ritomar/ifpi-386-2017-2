def somaH(n):
    h = 0 # Elemento neutro da soma
    for i in range(1, n + 1):
        h += 1/i
    return h


N = int(input("Digite N: "))
print("H = %.4f" % somaH(N))
