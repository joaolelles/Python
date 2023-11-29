def imc(peso, altura):
    result = peso / (altura / 100) ** 2
    print(result)
    if result < 18.5:
        print("Abaixo do peso")
    elif result < 24.9:
        print("Peso normal")
    elif result < 29.9:
        print("Acima do peso (sobrepeso)")
    elif result < 34.9:
        print("Obesidade I")
    elif result < 39.9:
        print("Obesidade II")
    else:
        print("Obesidade III")


imc(47, 162)
