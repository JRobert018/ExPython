lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)

    r = str(input("Deseja Continuar [S/N]")).upper()
    if r in "N":
        break

x = int(input("Informe o elemento que está procurando: "))

print(f"Vocẽ digitou {len(lista)} elementos.")

lista.sort(reverse=True)
print(f"A lista em ordem decrescente: {lista} ")

if x in lista:
    print(f"O valor {x} está presente na lista.")
else:
    print(f"O valor {x} não está presente na lista.")

