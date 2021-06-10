def run():
    #Es muy parecida la sintaxis de las listas a los diccionarios
    #lo que cambia es que al principio en vez de poner solo el valor que queremos agregar
    #hay que indicar la llave del diccionario y en vez de corchetes son llaves 
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 !=0}

    print(my_dict)

if __name__ == "__main__":
    run()