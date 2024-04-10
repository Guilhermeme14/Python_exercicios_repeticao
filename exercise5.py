anos = 0

while True:
    a = float(input("Digite o numero da população A: "))
    b = float(input("Digite o numero da população B: "))
    if a > b:
        print("População A tem que ser maior que B")
        continue
    taxa_crescimento_a = float(input("Digite a taxa de crescimento A (%): ")) / 100
    taxa_crescimento_b = float(input("Digite a taxa de crescimento B (%): ")) / 100
    if taxa_crescimento_a > taxa_crescimento_b:
        print("A taxa de crescimento A tem que ser maior do que da B")
        continue
    while a < b:
        anos += 1
        a = a + (a * taxa_crescimento_a)
        b = b + (b * taxa_crescimento_b)

    print(f"A população A ultrapassou a população B em {anos} anos.")
    