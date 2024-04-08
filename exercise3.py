nome = input("Digite o nome (maior que 3 caracteres): ")
while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente (maior que 3 caracteres): ")

idade = int(input("Digite a idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente (entre 0 e 150): "))

salario = float(input("Digite o salário (maior que zero): "))
while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente (maior que zero): "))

sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("Sexo inválido. Digite novamente ('f' ou 'm'): ").lower()

estado_civil = input("Digite o estado civil ('s', 'c', 'v' ou 'd'): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado civil inválido. Digite novamente ('s', 'c', 'v' ou 'd'): ").lower()

print("\nInformações válidas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo.upper()}")
print(f"Estado Civil: {estado_civil.upper()}")
