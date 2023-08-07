"""Calculadora com while"""
while True:
    first_number=input('Informe o primeiro número: ')
    second_number=input('Informe o segundo numero')
    operatro=input('Informe o operador(+-/*): ')
    numbers_validated=None
    f_number_float=0
    f_number2_float=0

    try:
        f_number_float=float(first_number)
        f_number2_float=float(second_number)
        numbers_validated=True

    except :
        numbers_validated=None
    
    if numbers_validated is None:
        print('Um ou ambos numeros informados são inválidos.')
        continue
    ###

    operated_permited= '+-/*'
    if operatro not in operated_permited:
        print('operador inválido')
        continue
    
    if len(operatro) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizando sua conta. confira o resultado abaixo')
    if operatro == '+':
        print(f'{f_number_float} +  {f_number2_float} =',f_number_float + f_number2_float)
    elif operatro == '-':
        print(f'{f_number_float} -  {f_number2_float} =',f_number_float - f_number2_float)
    elif operatro =='/':
        print(f'{f_number_float} /  {f_number2_float} =',f_number_float / f_number2_float)
    elif operatro == '*':
        print(f'{f_number_float} x  {f_number2_float} =',f_number_float * f_number2_float)
    
    else:
        print('Nunca deveria chegar aqui')

    sair=input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break