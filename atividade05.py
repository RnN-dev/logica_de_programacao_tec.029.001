nome = input("Informe seu nome: ")
nota1 = input("Informe sua primeira nota : ")
nota2 = input("Informe sua segunda nota : ")

nota1 = int(nota1)
nota2 = int(nota2)

media = (nota1 + nota2)/2

print(f"sua media é : {media}")

if media >= 7:
    print(f"{nome} está aprovado")
elif media >= 5:
    print(f"{nome} está de recuperação")
else:
    print(f"{nome} está reprovado")
