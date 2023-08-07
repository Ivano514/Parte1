frase= 'aaaooo'
i=0
qtd_apareceu_v=0
letra_apareceu_v=''

while i < len(frase):
    letra_atual=frase[i]

    if letra_atual==' ':
        i+=1
        continue
    qtd_aperceu_mais_vezes_atual= frase.count(letra_atual)
     
    if qtd_apareceu_v <= qtd_aperceu_mais_vezes_atual:
        qtd_apareceu_v = qtd_aperceu_mais_vezes_atual
        letra_apareceu_v= letra_atual

    i+=1

print('A letra que apareceu mais vezes foi '
          f'({letra_apareceu_v}) que apareceu '
          f'{qtd_apareceu_v}x')