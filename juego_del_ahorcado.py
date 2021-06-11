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
    
    # for i in range(len(caracteres)):
    #     print("__ ", end=" ")
    
    # print(caracteres)
    # adivina = input("\n\nAdivina la palabra :")
    

if __name__ == "__main__":
    run()