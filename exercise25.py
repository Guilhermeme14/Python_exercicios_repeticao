pessoas = int(input('Quantas pessoas: '))

idade = 0

for i in range(pessoas):
    n = float(input(f'Qual a idade da pessoa {i + 1}? '))
    idade += n

media = idade / pessoas

def media_idade(media):
    if media <= 25:
        return 'a galera é jovem'
    elif 25 > media <= 60:
        return 'a galera é adulta'
    elif 60 > media <= 120:
        return 'a galera é idosa'

print(f'A média de idade das pessoas é {media} ou seja {media_idade(media)}')