"""
Exercício
Peça ao usúario para digitar seu nome
Peça ao usúario para digitar sua idade
Se nome e idade forem digitados:
....Exiba:
..........Seu nome é {nome}
..........Seu nome invertido é {nome}
..........Seu nome contém(ou não) espaços
..........Seu nome tem {n} letras
..........A primeira letra do seu nome é {letra}
..........A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
......exiba "Descuplas, você digitou campos vazios."
"""


nome=str(input('Informe o seu nome: '))
idade= int(input('Informe  a sua idade: '))


if nome and idade:
    ...
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print("Seu nome contem espaços")
    else:
        print('Seu nome não contem espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    ...
    print('Desculpa mas voce digitou campo vazios')