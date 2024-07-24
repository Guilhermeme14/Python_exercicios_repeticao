notas = int(input('Quantas notas: '))

soma = 0

for i in range(notas):
    n = float(input(f'Digite a nota {i + 1}: '))
    soma += n

media = soma / notas

print(f'A média das notas é: {media}')
