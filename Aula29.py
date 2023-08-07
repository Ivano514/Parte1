"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str= input('vou dobrar o número que vc digitar: ')

try:
    print('STR:', numero_str)
    numero_float= float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float* 2}')

except:
    print('Não é um número')