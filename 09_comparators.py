'''
Los comandos >, <, >=, <=, == y != (diferente) se utilizan junto al comando print para evaluar
la veracidad de las relaciones plnteadas.
Estos operadores fallan con datos flotantes porque las operaciones entre ellos alteran los resultados.
Puede verse un ejemplo de comparación entre números flotantes en el archivo 10_float
'''

print(7 > 3)
print(3 > 7)
print (6 != 10)
print (6 == 10)
print ("Apple" == "Apple")
print ("Apple" == "apple")
print ("1" == 1)

age = 20
print(age >= 18)