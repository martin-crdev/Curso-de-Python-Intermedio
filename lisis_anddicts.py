def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"} 
    
#Super lista que contiene diccionarios
    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Facundo", "lastname": "Rodelo"},
        {"firstname": "Pepe", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"},
    ]

#Super diccionario que contiene listas en su interior
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

#con este for le decimos que vaya recorriendo al mismo tiempo las llaves y los valores con el metodo items
    for key, value in super_dict.items():
        print(key, "-", value)

#Con este for imprimimos los diccionarios de la lista super_list    
    for i in super_list:
        print(i["firstname"], "-", i["lastname"])

if __name__ == "__main__":
    run()