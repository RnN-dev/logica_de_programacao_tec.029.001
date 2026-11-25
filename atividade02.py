n1 = input("informe o primeiro numero : ")
n2 = input("informe o segundo numero : ")

n1 = int(n1)
n2 = int(n2)

soma = n1+n2
subtracao = n1-2
multiplicacao = n1*n2
divisao = n1 / n2
resto = n1 % n2

print(f"Soma : {soma}, {type(soma)}")
print(f"Subtracao: {subtracao}, {type(subtracao)}")
print(f"Multiplicacao: {multiplicacao}, {type(multiplicacao)}")
print(f"Divisao: {divisao}, {type(divisao)}")
print(f"resto: {resto}, {type(resto)}")