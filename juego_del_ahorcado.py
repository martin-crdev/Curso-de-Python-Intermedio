import random

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
   
    print(caracteres)

if __name__ == "__main__":
    run()