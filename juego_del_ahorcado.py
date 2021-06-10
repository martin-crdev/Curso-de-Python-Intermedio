def read():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for i, palabra in enumerate(f):
            palabras.append(palabra)
    print(palabras[169])


def run():
    read()

if __name__ == "__main__":
    run()