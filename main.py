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
En la clase 36 se trabaja nuevamente en el archivo principal
'''
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

# Para obtener el sangrado (ó indentación) necesario para el loop while se utiliza tab
rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    
    user_option = input('Piedra, papel o tijera => ')
    # La línea a continuación puede agregarse para evitar que el código se vea afectado
    # por la forma en que el usuario ingresa el texto, combinando mayúsculas y minúsculas
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opción no es válida')
        # La siguiente línea se incluye porque no es necesario ejecutar el resto del código
        continue

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
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computador ganó!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print ('papel gana a tijera')
            print ('usuario ganó!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Computador ganó!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print ('tijera gana a papel')
            print ('usuario ganó!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computador ganó!')
            computer_wins += 1
    
    print('Puntos para la computadora: ', computer_wins)
    print('Puntos para el usuario: ', user_wins)

    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if user_wins == 2:
        print('El ganador es el usuario')
        break

    rounds += 1

""" <Observación 1: Esta nota se incluye para indicar que algunos cambios en estos archivos se deben al trabajo ralizado en paralelo con GIT y GITHUB y que tienen por finalidad practicar los comandos de este software de control de versiones. """