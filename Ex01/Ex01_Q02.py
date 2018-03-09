def TesteIf(L1, L2, L3):
    letras = ''
    if L1 == 'V':
        letras = letras + 'A'
    else:
        if L2 == 'V':
            if L3 == 'V':
                letras = letras + 'B'
            else:
                letras = letras + 'C'
                letras = letras + 'D'
    letras = letras +'E'
    return letras

#Deve ser digitado apenas V ou F para leitura dos valores

La = input("Digite uma letra: ")
Lb = input("Digite uma letra: ")
Lc = input("Digite uma letra: ")

print(TesteIf(La, Lb, Lc))
