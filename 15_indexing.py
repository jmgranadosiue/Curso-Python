text = "Ella sabe Python"
print(text[0])
print(text[1])
# El siguiente comando muestra error porque no se corresponde con a longitud del texto
# print(text[999])

# Las siguientes líneas permiten identidicar el último caracter de la cadena en text
size = len(text)
print('size => ', size)
print(text[size - 1])
# Un resultado similar se obtiene con el siguiente comando
print(text[-1])

# slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:])
print(text[:])
print(text[10:16:1])
print(text[10:16:2])