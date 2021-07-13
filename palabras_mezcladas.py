import random
from random import shuffle

lista_palabras = ['perro', 'lobo', 'delfin', 'caballo', 'python', 'cobra', 'serpiente']


def presentacion_1():
    '''Devuelve el nivel en el que quiere jugar el usuario'''

    print("")
    print("                 Juego de Palabas")
    print("")
    print("")
    print("                 Adivina la palabra que puedes formar con las siguiente letras ")
    print("")
    print("")


def seguir_jugando():
    '''
    Devuelve True si el usuario quiere echar otra partida, sino devuelve False
    '''

    print("")
    restpuesta = input("        otra partida?").lower()
    if restpuesta == 's' or restpuesta == 'si':
        return True
    else:
        return False


def juego_nuevo():
    palabra_juego = random.choice(lista_palabras)
    palabras_desordenada = list(palabra_juego)
    shuffle(palabras_desordenada)

    print('palabras_desordenada: ', palabras_desordenada)
    while True:
        restpuesta = input("        intenta adivinar la palabra oculta: ").lower()
        print('ingresaste: {}'.format(restpuesta))

        if restpuesta == palabra_juego:
            print('gano!')
            return 0
        else:
            print('vuelvelo a intentar...')


presentacion_1()


partida = True
while partida:
    juego_nuevo()
    partida = seguir_jugando()