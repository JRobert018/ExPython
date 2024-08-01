valores = []

while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor aceito")
    else:
        print("Valores repetidos não serão inseridos.")
    r = str(input("Deseja continuar? [S/N]: ")).upper()
    if r in 'N':
        break
print("-"*30)
valores.sort()
print(f"{valores}")

