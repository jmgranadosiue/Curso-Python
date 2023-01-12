name = "Julian"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

'''
El comando print atomáticamente concatena varios string y es necesario utilizar la función str para convertir aquellas variables
que no sean de este tipo. En el archivo 04_string se utilizó la función f para dar formato y en ese contexto todas las variables
se interpretan como string.
str : para transformar a string
int : para transformar a entero
'''
age = 12
print("Mi edad es " + str(age))

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')