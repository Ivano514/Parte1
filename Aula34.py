"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> Quando um código não tem fim
"""
condicao=True
while condicao:
    nome =str(input('Qual é o seu nome:'))
    print(f'Seu nome é {nome}')
    
    if nome=='sair':

        break

print('Acabou')
