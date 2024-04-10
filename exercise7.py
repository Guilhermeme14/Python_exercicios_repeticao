n = [1, 3, 4, 5]

maior = n[0]

i = 1

while i < len(n):
    if n[i] > maior:
        maior = n[i]
    i += 1
print(maior)