frase='O Python é uma linguagem de programação'\
        ' multiparadigma. '\
        'Python foi criado por Guido Van Rossun'
i=0
apareceu_mais_vezes=0
letra_apareceu_mais_vezes=''
while i< len(frase):
    letra_aula= frase[i]
    quantas_vezes_letrras_aareceu= frase.count(letra_aula)

    if  apareceu_mais_vezes < quantas_vezes_letrras_aareceu:
        apareceu_mais_vezes = quantas_vezes_letrras_aareceu
        letra_apareceu_mais_vezes= letra_aula


    print('A letra que apareceu mais vezes foi'
          f'{letra_apareceu_mais_vezes} que apareceu'
          f'{apareceu_mais_vezes}')
    i+=1