ficha = []


while True:
    nome = str(input("Nome: "))

    nota1 = float(input("Nota 1: "))

    nota2 = float(input("Nota 2: "))

    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])

    continuar = str(input("Deseja continuar: [S/N]")).upper()
    if continuar in 'N':
        break
print('---'*30)
print(f"{"No.":<4}{"NOME":<10} {"MÈDIA":>8}")
for i,a in enumerate(ficha):
    print(f"{i+1:<4}{a[0]:<10}{a[2]:>8.1f}")

while True :
    opc= int(input("Mostrar nota de qual aluno? (999 encerra o programa.) "))
    if opc == 999:
        print("Finalizado")
        break
    elif opc <= len(ficha):
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")



