from  random import  randint
lista = []
jogos = []
print('-'*30)
print('         Mega Sena      ')
print('-'*30)

quant = int(input("Quantos jogos você quer jogar: "))
total = 1 # contador do total de jogos.
while total <= quant:# roda até o contador for menor ou igual a quantidade solicitada.
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:# verifica se o número está na lista, caso não esteja ele será adcionado.

            lista.append(num)

            cont += 1# toda vez que um numero é adicionado ele soma 1 no contador.

        if cont >= 6:# E quando o contador bater o limite de 6, ele para e vai para o próximo jogo.
            break
    lista.sort()#deixa em ordem crecente

    jogos.append(lista[:])#Cria uma copia da lista para lista jogos.

    lista.clear()#limpa a lista para o próximo jogo

    total += 1# toda vez que um jogo for completado ele soma 1 até bater o limite do usuáro.
print('-='*3, f'SORTEANDO {quant} JOGOS','-='*3)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

