"""
Iterando Strings com while
"""
#......01234567891011
name= 'Mateus Ivano' #Iteravéis


indice=0
new_name=''
while indice < len(name):
    letter=name[indice]
    new_name += f'*{letter}'
    indice+=1

print(new_name)

