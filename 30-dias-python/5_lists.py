# lists
"""
Hay cuatro tipos de datos de coleccion en python:
* List: es una coleccion ordenada y cambiable (modificable). Permite miembros duplicados.
* Tuple: es una coleccion ordenada e inmutable o inmodificable (inmutable).
* Set: es una coleccion desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
* Dictionary: es una coleccion desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.

Una lista es una coleccion de diferentes tipos de datos ordenados y modificables (mutables). Una lista puede estar vacia o puede tener diferentes elementos de tipo de datos.
"""
# Como crear una lista
"""
En python podemos crear lista de dos formas:
* Uso de la funcion incorporada de lista
"""
# syntax
lst = list()

empty_list = list()
print(len(empty_list))

# Usando corchetes, []
# syntax
lst = []

empty_list = []
print(len(empty_list))

# Lista con valores iniciales. Usamos len() para encontrar la longitud de una lista.
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "NodeJS", "mMongoDB"]
countries = ["Finland","Estonia", "Denmark", "Sweden", "Norway"]
# print the lists and its length
print("Fruits: ", fruits)
print("Number of fruits: ", len(fruits))
print("Vegetables: ", vegetables)
print("Number of vegetables: ", len(vegetables))
print("Animal products: ", animal_products)
print("Number of animal products: ", len(animal_products))
print("Web technologies: ", web_techs)
print("Number of web technologies: ", len(web_techs))
print("Countries: ", countries)
print("Number of countries: ", len(countries))

# Las listas pueden tener elementos de diferentes tipos de datos
lst = ["Gustavo", 25, True, {"country":"Peru", "city":"Lima",}]

# Acceder a los elementos de la lista mediante la indexacion positiva
"""
Accedemos a cada elemento de una lista utilizando su indice. El indice de una lista comienza desde 0.
"""
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Acceder a los elementos de la lista mediante la indexacion negativa
"""
La indexacion negativa significa comenzar desde el final, -1 se refiere al ultimo elemento, -2 se refiere al penultimo elemento.
"""
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)

# Desempaquetar elementos de la lista
lst = ["item", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, * rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# First Example
fruits = ["banana", "orange", "mango", "lemon", "lime", "apple"]
first_fruit, second_fruit, third_fruit, * rest = lst
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

# Second Example about unpacking list
first, second, third, * rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Third Example about unpacking list
countries = ["Germany", "France", "Belgium", "Sweden", "Denmark", "Finland", "Norway", "Iceland", "Estonia"]
gr, fr, bg, sw, * scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Cortar elementos de una lista
"""
indexacion positiva: podemos especificar un rango de indices positivos.
especificando el ndice, el final y el paso, el valor de retorno sera una nueva lista.
(valores predeterminados para inicio = 0, final = len (lst) - 1 (ultimo elemento), paso = 1)
"""
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]
# this will also give the same result as the one above
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_and_lemon = fruits[1:]
orange_and_lemon = fruits[::2]

# indexacion negativa: podemos especificar un rango de indices negativos. especificando el inicio, el final y el paso, el valor de retorno sera una nueva lista
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_and_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

# Modificacion de listas
"""
Lista es una coleccion ordenada mutable o modificable de elementos.Vamos a modificar la lista de frutas.
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)
fruits[1] = "apple"
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

# comprobacion de elementos en una lista
"""
comprobacion de un elemento si es miembro de una lista mediante el operador in.
Ejemplo:
"""
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)

# Adicion de elementos a una lista
"""
Para agregar un elemento al final de una lista existente, usamos el metodo
append().
"""
# syntax
"""
lst = list()
lst.append(item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

# insertar elementos en una lista
"""
Podemos usar el metodo insert() para insertar un solo elemento en un indice especifico en una lista. Tenga en cuenta que otros elementos se desplazan a la derecha, Los metodos insert() toman dos argumentos: indice y un elemento para insertar.
"""
"""
# syntax
lst = ["item1", "item2"]
lst.insert(index, item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")
print(fruits)
fruits.insert(3, "lime")
print(fruits)

# Eliminacion de elementos de una lista
"""
El metodo de eliminacion elimina un elemento especifico de una lista.
# syntax
lst = ["item1", "item2"]
lst.remove(item)
"""
fruits = ["banana", "orange", "mango", "lemon", "banana"]
fruits.remove("banana")
print(fruits)
fruits.remove("lemon")
print(fruits)

# Eliminacion de elementos mediante Pop
"""
El metodo pop() elimina el indice especificado (o el ultimo elemento si no se especifica el indice):
# syntax
lst = ["item1", "item2"]
lst.pop()
lst.pop(index)
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

# Eliminacion de elementos mediante Del
"""
La palabra clave del elimina el indice especificado y tambien se puede usar para eliminar elementos dentro del rango del indice. Tmabien puede eliminar la lista por completo.
# syntax
lst = ["item1", "item2"]
del lst[index]
del lst
"""
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
print(fruits)

# Elementos de la lista de compensacion
"""
El metodo clear() vacio la lista:
# syntax
lst = ["item1", "item2"]
lst.clear()
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)

# Copiar una lista
"""
Es posible copiar una lista reasignandola a una nueva variable de la siguiente forma: lista2 = list1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 tambien modificara el original, list2.
Pero hay muchos casos en los que no nos gusta modificar el original sino que nos gusta tener una copia diferente. Una forma de evitar el problema anteriror es usar copy().

# syntax
lst = ["item1", "item2"]
lst_copy = lst.copy()
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)

# Unirse a listas
"""
Hay varias formas de unir o concatenar dos o mas listas en Python.
* Operador mas (+)
# syntax
list3 = list1 + list2
"""
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Patato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# joining using extend() method The extend() method allows to append list in a list. See the example below.
"""
# syntax
list1 = ["item1", "item2"]
list2 = ["item3", "item4", "item5"]
list1.extend(list2)
"""
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers: ", num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers: ", negative_numbers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits.extend(vegetables)
print("Fruits and vegetables: ", fruits)

# Counting Items in a List
"""
El metodo count() devuelve el numero de veces que aparece un elemento en una lista:
# syntax
lst = ["item1", "item2"]
lst.count(item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Encontrar el indice de un elemento
"""
El metodo index() devuelve el indice de un elemento de la lista:
# syntax
lst = ["item1", "item2"]
lst.index(item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# Invertir una lista
"""
El metodo reverse() invierte el orden de una lista.
# syntax
lst = ["item1", "item2"]
lst.reverse()
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# clasificacion de elementos de la lista
"""
Para ordenar listas, podemos usar el metodo sort() o las funciones integradas sorted().
El metodo sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del metodo sort() reverse es igual a verdadero, ordenara la lista en orden descendente.
"""
# sort(): este metodo modifica la lista original
"""
# syntax
lst = ["item1", "item2"]
lst.sort()
lst.sort(reverse = True)
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse = True)
print(ages)

# sorted(): devuelve la lista ordenada sin modificar la lista original
# Ejemplo:
fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))
# Reverse order
fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)