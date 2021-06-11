import random
import os

def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def read():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for i, palabra in enumerate(f):
            palabras.append(palabra)
    palabra_random = random.choice(palabras)
    return palabra_random

def seperar_caracteres(palabra):
    caracteres = []
    for caracter in palabra:
        caracteres.append(caracter)
    num_caracteres = len(caracteres)-1
    caracteres.pop(num_caracteres)
    return caracteres


def run():
    palabra = read()
    caracteres = seperar_caracteres(palabra)
    ahorcado = []

    for letra in caracteres:
        ahorcado.append("__ ")
    while ahorcado != caracteres:
        borrar_pantalla()    
        for i in range(len(ahorcado)):
            print(ahorcado[i], end=" ")
        print(caracteres)
    
        adivina = input("Adivina la palabra: ")

        for index, value in enumerate(caracteres):
            if value == adivina:
                ahorcado[index] = adivina
    print("Ganaste")
    
if __name__ == "__main__":
    run()