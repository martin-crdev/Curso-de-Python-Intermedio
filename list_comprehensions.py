def run():
    #
    # squares = []              creamos una lista vacia
    # for i in range(1, 101):   creamos in ciclo for que incremente del 1 al 100
    #     if i % 3 != 0:        si i modulo 3 es distinto a 0 es decir que no es divisble entre 3
    #         squares.append(i**2)  añade a la lista el cuadrado de ese numero 
    
    #i al cuadrado, para todas las i dentro del rango de 1 a 101

    #solo si i % 3 es distinto a 0
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

if __name__ == "__main__":
    run()