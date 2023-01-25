# while True:
#     print('se ejecuó')

# counter = 0

# while counter < 10:
#     counter += 1
#     print(counter)

# counter = 0

# # El comando break muestra una manera de detener un loop
# while counter < 20:
#     counter += 1
#     if counter == 15:
#         break
#     print(counter)

counter = 0

# El comando continue hace que no se ejecute lo que está después de él y dando paso a la siguiente iteración
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)