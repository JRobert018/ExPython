matriz = [[0]*3 for _ in range(3)]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um número para casa [{linha},{coluna}]: "))
print('---'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end= '')
    print()