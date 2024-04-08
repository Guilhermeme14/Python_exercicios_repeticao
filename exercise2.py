usuario = "dedo"
senha = "1234"

while True:
    usuario_ = input("Digite o nome do usuário: ")
    senha_ = input("Digite a senha: ")
    
    if usuario_ != usuario:
        print("Usuario incorreto!")
    
    elif senha_ != senha:
        print("Senha incorreta!")
    
    else:
        print("Acesso autorizado")
        break
