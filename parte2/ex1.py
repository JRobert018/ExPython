lista_geral = []
dados_lista = []
mai = men = 0

cont = 0
while True:
    dados_lista.append(str(input("Digite seu nome: ")))
    dados_lista.append(float(input("Digite se peso: ")))
    if len(lista_geral) == 0:# se o tamnaho da lista for = 0 ele define maior e menor como indeci 1 da lista.
        mai = men = dados_lista[1]
    else:
        if dados_lista[1] > mai:
            mai = dados_lista[1]

        elif dados_lista[1] < men:
            men = dados_lista[1]

    lista_geral.append(dados_lista[:])
    dados_lista.clear()

    cont += 1
    if cont == 3:
        continuar = str(input("Deseja continuar [S/N]: ")).upper()
        if continuar in 'N':
            break
        else:
            cont = 0

print('-'*30)
print(f"{len(lista_geral)} pessoas foram cadastradas")
for i in lista_geral:
    print(f"{i[0]} com peso {i[1]}")
print('-'*30)
print(f"O maior ṕeso foi de {mai}kg. peso de ", end = ' ')
for p in lista_geral:
    if p[1] == mai:
        print(f"[{p[0]}]",end='')
print()
print(f"O menor peso foi de {men}kg. peso de ", end = ' ')
for p in lista_geral:
    if p[1] == men:
        print(f"[{p[0]}]",end='')
print()
