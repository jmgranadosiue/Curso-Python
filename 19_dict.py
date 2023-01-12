my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': "bla bla bla",
    'name': 'Julian',
    'last_name': 'Molina Monroy',
    'age': 87
}

print(my_dict)

# Longitud del diccionario
print(len(my_dict))
# Imprimir el valor asociado a la clave 'age' o a la clave 'last_name'
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('last_name'))

# La ventaja de utilizar el atributo get es que si se ingresa una llave inexistente el comando lo informa mientras que el comando
# print(my_dict['last_name']) muestra un error en la terminal
print(my_dict.get('unvalor'))

print('avion' in my_dict)
print('otroqueno' in my_dict)