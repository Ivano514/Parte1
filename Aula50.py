"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
.......append, insert, pop, del, clear, extend, +
Create Read Upadte .... Delete
Criar, ler, alterar, ....apagar = list [i] (CRUD)
"""

lista= [10, 20, 30, 40]
lista[2]=300

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor=lista.pop(3)
print(lista, 'Removido', ultimo_valor)
