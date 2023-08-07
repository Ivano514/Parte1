"""
Faça um jogo para o usúario adivinhar qual a palavra secreta.
-Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para  o usúario digitar uma letra.

-Quando o usúario digitar uma letra, você vai conferir se aletra digitada 
está  na palavra secreta.

......-Se a letra digitada estiver na palavra secreta; exiba a letra;
......-Se a letra digitada não estiver na palavra secreta; exiba *.

Faça contagem de tentativas do seu usúario
"""

import os


palavra_secreta='Japão'
letras_acertadas= ''
tentativas=0
while True:
    palavra=input('Digite uma letra: ')
    tentativas+=1

    if len(palavra) > 1:
        print('Informe apenas uma letra')
        continue
    
    if palavra in palavra_secreta:
        letras_acertadas+=palavra

    palavra_formada= ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada +='*'
    print('Palavra formada:' ,palavra_formada)
    if  palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS')
        print('A palavra era: ',palavra_secreta)
        print('Tentativas', tentativas)
        letras_acertadas= ''
        tentativas=0