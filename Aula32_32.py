"""
Faça um programa que peça ao úsuario para digitar um número inteiro,
informe se este número é par ou impar. Caso o úsuario não digite um número
inteiro, informe que não é um número inteiro
"""
try:
    number=int(input('Informe um número inteiro'))

    if number %2:
        print("É um número impar")
    else:
        print('É um número inteiro')
except:
    print('Não é um número inteiro')

"""
Faça um programa que pergunta a hora ao usúario e, baseando-se no horário
descrito, exiba a saudaçao apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23 
"""
try:
    hour=int(input('Informe que horas são: '))
    if hour >= 0 and hour <= 11:
        print('Bom dia')

    elif hour >= 12 and hour <=17:
        print('Boa tarde')

    elif hour >= 18 and hour <= 23:
        print('Boa noite')

except:
    print("Por favor digite um número")

"""
Faça um programa que peça o primeiro nome do usuário.Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto": se tiver 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande 
"""

name_user=str(input('Informe o seu nome: '))
if len(name_user) <= 4:
    print('Seu nome é curto')
elif len(name_user) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')