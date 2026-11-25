nome = input("Informe seu nome : ")
idade = input("Informe sua idade : ")

idade = int(idade)

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")
