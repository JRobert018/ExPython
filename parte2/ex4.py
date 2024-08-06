matriz = [[0]*3 for _ in range(3)]
soma_pares =  maior_valor = soma_coluna = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para posição [{linha} , {coluna}]: "))

print('----'*30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
for linha in range(0,3):
    soma_coluna += matriz[linha][2]

maior_valor = max(matriz[1][coluna]for coluna in range(0,3))# o for dentro da max ira percorrer todas as colunas da linha
#1  e irá armazenar o maior valor.


print('----'*30)
print(f"A soma dos valores pares da matriz é igual a: {soma_pares}")
print(f"A soma da coluna 3 é igual a: {soma_coluna}")
print(f"O maior valor da linha 2 é: {maior_valor}")
