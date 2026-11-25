massa = input("Informe a massa : ").replace(",",".")
altura = input("Informe sua altura : ").replace(",",".")


altura = float(altura)
massa = float(massa)

if massa <= 140:
    if altura >= 1.15:
        print("Entrada do usuario permitida")
    else: 
        print("Entrada do usuário negada")
else:
    print("entrada do usuário negada")