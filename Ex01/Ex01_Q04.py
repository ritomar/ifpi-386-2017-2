def imprimeOrdenado(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a, b, c)

imprimeOrdenado(6, 8, 5)
