# Creación del diccionario
person = {
    'name' : 'Julián',
    'last_name' : 'Granados',
    'langs': ['python', 'javascript'],
    'age': 41
}
print(person)

# Modificación de algunos valores del diccionario
person['name'] = 'Mauricio'
person['age'] += 1
person['langs'].append('rust')
print(person)

# Eliminación de un ítem del diccionario
del person['last_name']
print(person)
# También es posible eliminar un ítem utilizando el atributo pop. 
# En el caso de los diccionarios, este comando requiere un argumento a través del cual se le informa el elemento a eliminar.
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())