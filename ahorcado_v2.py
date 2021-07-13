import random
import time

## Listas de palabras
marcas_de_carros = ["ford", "honda", "nissan", "renault", "chevrolet", "BMW", "lexus"]

nombres_de_paises = ["colombia", "mexico", "ecuador", "panama", "uruguay", "guatemala"]

nombres_de_personajes_de_disney = ["mickey mouse", "stich", "woody", "buzz ligthyear", "pato donald", "spiderman",
                                   "goofy", "simba"]

nombres_de_youtubers_de_free_fire = ["donato", "luay", "antronix", "domidios", "punisher", "fernanfloo", "mrstiven",
                                     "assias", "epidemic", "diana tc", "roberth ceballos", "the nino"]

print("bienvenidos al juego del ahorcado")
time.sleep(2)
print("el objetivo del juego es que adivines las palabras ocultas letra por letra")
print("inicias el juego con 5 vidas cada vez que introduzcas una letras que no va en la palabra se restara una vida")
time.sleep(2)
palabra_secreta = ""
while not palabra_secreta:
    print("""con que tematica desea jugar hay 4 tematicas de juego para q eligas introduce el numero
    1 si deseas la tematica de marcas de carros
    introduce el numero 2 si deseas la de nombres de paises
    introduce el numero 3 si deseas de nombres de personajes de disney
    e introduce el numero 4 si deseas nombres de youtubers de free fire""")
    time.sleep(2)

    cat_seleccionada = input("Ingrese su numero segun la tematica que desea jugar")

    if cat_seleccionada == "1":
        print("excelente has seleccionado la tematica de marcas de carros")
        palabra_secreta = random.choice(marcas_de_carros)
    elif cat_seleccionada == "2":
        print("Excelente has seleccionado la categoria de nombres de paises")
        palabra_secreta = random.choice(nombres_de_paises)
    elif cat_seleccionada == "3":
        print("Excelente has seleccionado la categoria de personajes de disney")
        palabra_secreta = random.choice(nombres_de_personajes_de_disney)
    elif cat_seleccionada == "4":
        print("Excelente has seleccionado la categoria de youtubers de free fire")
        palabra_secreta = random.choice(nombres_de_youtubers_de_free_fire)

    else:
        print("por favor selecciona una categoria valida")
        cat_seleccionada = input("Ingrese un numero segun la tematica que desee jugar")
print('palabra_secreta', palabra_secreta)
## Es el numero de veces que se puede equivocar
vidas = 5

lista_letras_intentos = []
lista_letras_adivinadas = []

##imprimos la palabra sin letras
print('_' * len(palabra_secreta))

while True:
    while True:
        letra_intento = input("adivina una letra: ").lower()
        lista_letras_intentos.append(letra_intento)
        if letra_intento in lista_letras_intentos:
            print("ya habias intentado con esa letra intenta con otra")
        else:
            if letra_intento in palabra_secreta:
                print("felicidades adivinaste una letra")
                lista_letras_adivinadas.append(letra_intento)
            else:
                vidas = vidas - 1
                print("te haz equivocado y perdido una vida")
                print("te quedan " + str(vidas) + "palbra_secreta")

            estatus_actual = " "

            letras_faltantes = 0
            for letra in palabra_secreta:
                if letra in lista_letras_adivinadas:
                    estatus_actual = estatus_actual + letra

                else:
                    estatus_actual = estatus_actual + letra

                # else:
                #     estatus_actual = estatus_actual + " "
                #     letras_faltantes = letras_faltantes + 1

            ##imprimir palabra con algunas letras
        print(estatus_actual)

        if letras_faltante == 0:
            print("Felicidades haz ganado")
            print("la palabra secreta es: + palabra_secreta")
            break