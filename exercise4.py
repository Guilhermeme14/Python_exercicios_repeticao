a = 80000
b = 200000

anos = 0

while a < b:
    crescimento_a = a * 0.03
    crescimento_b = b * 0.015
    anos += 1
    a = a + crescimento_a
    b = b + crescimento_b
    
print(f"A população A chegou a {a: .0f} de pessoas e a população B chegou a {b: .0f} de pessoas em {anos} anos")
      
     
