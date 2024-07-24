n = int(input("Digite um número: "))

divisores = []
for x in range(2, int(n ** 0.5) + 1):
    if n % x == 0:
        for x in range(1, n + 1):
            if n % x == 0:
                divisores.append(x)
        print(f'{n} não é um número primo e é divisível por {divisores}')
    else:
        print(f"{n} é um número primo")