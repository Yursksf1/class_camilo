import time
import random
nombre = input("como te llamas ")

print("hola, "+ nombre +" es hora de jugar")
print(" ")
time.sleep(1)

print("comienza a adivinar")
time.sleep(0.5)

posibles_palabras = ['cocodrilo', 'tortuga', 'serpiente', 'lagartija', 'iguana']
palabra = random.choice(posibles_palabras)
tupalabra = " "
vidas = 5

while vidas > 0:
    fallas = 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("*", end="")
            fallas += 1

    if fallas == 0:
        input()
        print("")
        print("felicidades, ganaste")
        input()
        break

    print("")
    tuletra = input("introduce una letra: ")
    tupalabra += tuletra

    if tuletra not in palabra:
        vidas -= 1
        print("equivocacion")
        print("tu tienes " + str(vidas) +" vidas")
    if vidas == 0:
        print("perdiste!")
    else:
        input()
        print("gracias por participar")
        input()
