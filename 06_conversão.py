nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
altura = input("Informe sua altura: ").replace(',','.')

idade = int(idade)
altura = float(altura)


print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura}. Tipo: {type(altura)}")