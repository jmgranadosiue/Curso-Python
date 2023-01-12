numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dish', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

text = 'Hola'
## La siguiente línea genera un mensaje de error porque no es posible sobreescribir las partes de un string
#text[0] = 'W'
## Pero esto sí es posible en las listas como se hace con los siguientes comandos
tasks [0] = 'watch platzi courses'
print(tasks)

print(numbers[:3])

print(True in types)
print('hola' in types)