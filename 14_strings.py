text = 'Ella sabe programar en Python'

'''
# Busca el texto ingresado en la variable tipo string.
  Si hace parte imprime True, en caso contrario imprime False.
print('Javascript' in text)
print('Python' in text)

if 'JS' in text:
    print('Elegiste bien!')
else:
    print('También elegiste bien')
'''

# mide la cadena de caracteres en text
size = len(text)
print(size)

print(text)
# Escribe todos los caracteres en mayúscula
print(text.upper())
# Escribe todos los caracteres en minúscula
print(text.lower())
# Cuenta el número de veces que aparece el caracter en la variable text.
print(text.count('a'))
# Cambia mayúsculas a minúsculas y minúsculas a mayúsculas
print(text.swapcase())
# Evalúa si la cadena de caracteres inicia con el texto ingresado
print(text.startswith('Ella'))
# Evalúa si la cadena de caracteres finaliza con el texto ingresado
print(text.endswith('Rust'))
# Reemplaza el primer texto con el segundo
print(text.replace('Python', 'Go'))

text_2 = 'este es un título'
print(text_2)
# Escribe en mayúscula la primera letra de la cadena de caracteres
print(text_2.capitalize())
# Escribe en mayúscula la primera letra de cada palabra
print(text_2.title())
# Evalúa si la cadena de caracteres es un número
print(text_2.isdigit())
print("398".isdigit())