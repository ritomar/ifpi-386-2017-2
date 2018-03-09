def Mensagem():
    x = 10
    y = 1
    x -= 1
    y += 2
    x = x - 1
    y = y + 2
    x = x - 1
    y = y + 2
    if x > y:
        return "x ficou maior que y"
    elif x < y:
        return "x ficou menor que y"
    else:
        return "x e y ficaram iguais"

print(Mensagem())
