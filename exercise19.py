lista = []
n = int(input("Digite o número de números do conjunto: "))

for i in range(n):
    i = int(input("Digite o numero: "))
    if i >= 1000 or i <= 0:
        msg = True
        break
    else:
        lista.append(i)
if msg is not True:
    soma = 0
    menor = lista[0]
    maior = lista[0]

    for x in lista:
        if x < menor:
            menor = x
        if x > maior:
            maior = x
        soma += x

    print(menor)
    print(maior)
    print(soma)
else:
    print("Número inválido")
