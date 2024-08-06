valores = []
for i in range(0,5):
    valores.append(int(input(f"Digite um valor para posição {i} : ")))


print(f"Você digitou os valores {valores}")
print(f"Sendo o maior valor da lista o número {max(valores)} na posição {valores.index(max(valores))}")
print(f"Sendo o menor vallor da lista o número {min(valores)} na posição {valores.index(min(valores))}")
