n = int(input("Digite um número: "))

for x in range(2, int(n ** 0.5) + 1):
    if n %x == 0:
        print(f"{n} não é um número primo")
    else:
        print(f"{n} é um número primo")