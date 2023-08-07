entrada= input('[E]ntrar [S]air: ')
senha_digitada= input("senha: ")
senha_permitida='123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print("entrar")
else:
    print("Sair")