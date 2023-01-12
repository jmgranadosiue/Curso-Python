# CRUD: Create, Read, Update and Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1]=10
print(numbers)

# El comando append permite agregar nuevos elementos al final de una lista
numbers.append(700)
print(numbers)

# El comando insert permite agregar nuevos elementos a una lista eligiendo la posición (no necesariamente al final de la lista)
numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

# Unión de dos listas
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list=numbers + tasks
print(new_list)

# Identificar la posición de un elemento en una lista y actualizar la posición
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

# Remover elementos de una lista
new_list.remove('todo 1')
print(new_list)

# Remover el último elemento de una lista o el elemento en una posición determinada
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)

# Invertir el orden de una lista
new_list.reverse()
print(new_list)

# Ordenar una lista
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)
strings = ['Re', 'Ab', 'Ed']
strings.sort()
print(strings)
## No es posible ordenar una lista que contiene diferentes tipos de elementos. La siguiente línea genera un mensaje de error.
# new_list.sort()