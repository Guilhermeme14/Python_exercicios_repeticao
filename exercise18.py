lista = [1, 6, 2, 9, 4]
soma= 0
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