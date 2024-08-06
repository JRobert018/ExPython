lista = []
lista_par = []
lista_impar = []

cont = 0#contador
while True:
    conteudo_lista = int(input("Digite um valor: "))
    lista.append(conteudo_lista)
    if conteudo_lista % 2 == 0:

        lista_par.append(conteudo_lista)
    else:
        lista_impar.append(conteudo_lista)
    cont += 1
    if cont == 3:# toda vez que o contador for igual a 3 ele vai perguntar se deseja continuar.
        resposta = str(input("Deseja continuar [S/N]: ")).upper()
        cont = 0

        if resposta in 'N':
            break
print(f"A lista completa é composta pelos seguintes elementos: {lista}")
print(f"lista com elementos pares: {lista_par}")
print(f"lista com elementos impares: {lista_impar}")
