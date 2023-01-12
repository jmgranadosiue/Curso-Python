print("Hola, esto es python")
print("Hola, soy Julián y tengo 41 años")

# Operaciones . . . 

print(12 + 5)
print(10-5)
print(2*6)
print(10/3)

# Esto es un comentario corto

"""
Los comentarios extensos que requieren varias
lineas de código pueden incluirse utilizando
triples comillas dobles o sencillas.
"""

'''
Esta es la otra posibilidad para ingresar
comentarios extensos que requieren varias 
líneas de comando
'''

# *****************************************************

'''
En la clase 20 se regresa a trabajar en el archivo principal
En la clase 28 se trabaja nuevamente en el archivo principal
'''
import random

options = ('piedra', 'papel', 'tijera')

user_option = input('Piedra, papel o tijera => ')
# La línea a continuación puede agregarse para evitar que el código se vea afectado
# por la forma en que el usuario ingresa el texto, combinando mayúsculas y minúsculas
user_option = user_option.lower()

if not user_option in options:
    print('Esa opción no es válida')

# # La siguiente línea se modifica en la clase 28 para utilizar la librería random
# computer_option = 'papel'
computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print ('piedra gana a tijera')
        print ('usuario ganó!')
    else:
        print('Papel gana a piedra')
        print('Computador ganó!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print ('papel gana a tijera')
        print ('usuario ganó!')
    else:
        print('tijera gana a papel')
        print('Computador ganó!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print ('tijera gana a papel')
        print ('usuario ganó!')
    else:
        print('piedra gana a tijera')
        print('Computador ganó!')