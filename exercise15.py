n = int(input("Digite o valor de n para gerar a série de Fibonacci até o n-ésimo termo: "))

fib_sequence = [1, 1]
for i in range(2, n):
    next_term = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_term)

fibonacci_series = fib_sequence[:n]
print(f"A série de Fibonacci até o {n}-ésimo termo é:", fibonacci_series)
