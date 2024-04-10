n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
i = n1 + 1
while n1 < i < n2:
    soma = i + i
    print(i)
    i+=1
print(soma)