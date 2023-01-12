if True:
    print('Debe ejecutarse')

if False:
    print('No debe ejecutarse')

pet = input('¿Cuál es tu mascota favorita?')


if pet == 'perro':
    print('genial tienes buen gusto')

if pet == 'gato':
    print('espero que tengas suerte')

if pet == 'perro':
    print('genial tienes buen gusto')
elif pet == 'gato':
    print('espero que tengas suerte')
elif pet == 'pez':
    print('eres lo máximo')
else:
    print('no tienes mascotas interesantes')

stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')
