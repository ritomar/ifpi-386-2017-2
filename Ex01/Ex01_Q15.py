def imc(massa, altura):
    return massa / (altura * altura)


def msg_imc(imc_calculado):
    if imc_calculado < 18.5:
        return "Abaixo do peso"
    elif imc_calculado < 25:
        return "Peso normal"
    elif imc_calculado < 30:
        return "Sobrepeso"
    elif imc_calculado < 35:
        return "Obeso leve"
    elif imc_calculado < 40:
        return "Obeso moderado"
    else:
        return "Obeso mórbido"


p = float(input("Digite seu peso: "))
h = float(input("Digite sua altura:"))

print(msg_imc(imc(p, h)))
