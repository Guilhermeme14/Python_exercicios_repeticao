n = int(input("Digite o numero que quer ver na tabuada: "))
i = 0

print(f"Tabuada do {n}")

while i < 10:
    i += 1
    tabuada = n * i
    print(f"{n} x {i} : {tabuada}")