gasolina = float(input("Digite o valor da gasolina: ").replace(",","."))
etanol = float(input("Digite o valor do etanol: ").replace(",","."))

if etanol <= gasolina * 0.75:
    print("Compensa abastecer com etanol!")
else:
    print("Compensa abastecer com gasolina!")
