number = int(11)
divisores=[]
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            for x in range(1, number + 1):
                if number % x == 0:
                    divisores.append(x)
            print(number, 'não é primo e é divisível por', *divisores)
            
    else:
        print(number, 'é primo')
