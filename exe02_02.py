nome = input("Informe seu Nome: ")
massa = input("Informe sua massas: ")
altura = input("Informe sua altura: ").replace(",",".")

nome = str(nome)
massa = int(massa)
altura = float(altura)

imc = massa/(altura**2)

print(imc)

if imc < 18.5:
    print("Usuario abaixo do peso")
elif imc < 25:
    print("usuario esta no peso ideal")
elif imc < 35:
    print("usuario esta obeso")
elif imc < 40:
    print("usuario está com obesidade nivel 2")
else:
    print("usuario esta com obesidade morbida")