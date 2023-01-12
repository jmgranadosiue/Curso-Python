numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

# Comando para acceder a una posición partiular de una tupla
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])

# # Las tuplas no permiten agregar información como puede hacerse en las listas. La siguiente línea genera un mensaje de error.
# numbers.append(10)
# # Tampoco es posible modificar sus entradas. La siguiente línea genera un mensaje de error.
# numbers[1] = 'change'

print(strings)
# Posición en la que aparece 'zule'
print(strings.index('zule'))
# Número de veces que se repite 'nico'
print(strings.count('nico'))

# Es posible transformar entre tuplas y listas. Transformación de tupla a lista.
my_list = list(strings)
print(type(my_list))
print(my_list)
# Transformación de lista a tupla.
my_tuple = tuple(my_list)
print(type(my_tuple))

# Puede consultarse la aplicación de las tuplas en el archivo main.py