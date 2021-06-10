def run():

    #imprime el diccionario del 1 al 1000 y guarda su raiz cuadrada
    my_dict = {i: i**.5 for i in range(1, 1001) }

    print(my_dict)

if __name__ == "__main__":
    run()

# Uso con filter

# my_list = [1,4,5,6,9,13,19,21]

# odd = list(filter(lambda x: x%2 !=0, my_list))

# print(odd)

# Uso con map 

# my_list = [1,2,3,4,5]

# squares = list(map(lambda x: x**2, my_list))

# print(squares)

# Uso con reduce

# from functools import reduce

# my_list = [2,2,2,2,2]

# all_multiplied = reduce(lambda a, b: a*b, my_list)

# print(all_multiplied)