condicao=True
passou_if=None

if condicao:
    passou_if=True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_if is None:
    print('Não passou no if')
if passou_if is not None:
    print('Passou no if')