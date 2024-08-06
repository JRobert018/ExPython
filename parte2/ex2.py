lista_geral = [[],[]]#lista com 2 lista inclusas
valor = 0
for i in range(0,7):
    valor = int(input(f"Digite o {i+1} valor: "))
    if valor % 2 == 0:
        lista_geral[0].append(valor)
    else:
        lista_geral[1].append(valor)
print('---'*30)
lista_geral[0].sort()
lista_geral[1].sort()
print(f"Os valores pares foram {lista_geral[0]}")
print(f"Os valores impares foram {lista_geral[1]}")
