# tuplas
"""
Una tupla es una coleccion de diferentes tipos de datos ordenados e inmutables (inmutables).
Las tuplas se escriben con corchetes, (). Una vez que se crea una tupla, no podemos cambiar sus valores. No podemos usar metodos de agregar, insertar, eliminar en una tupla porque no es modificable (mutable). A diferencia de list, tuple tiene pocos metodos. Metodos relacionados con las tuplas:
* tuple(): para crear una tupla vacia
* count(): para contar el numero de un elemento especifico en una tupla
* index(): para encontrar el indice de un elemento especifico en una tupla
* operator: unir dos o mas tuplas y crear una nueva tupla
"""
# Crear una tupla
"""
* tupla vacia: creacion de una tupla vacia
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
"""
# * tupla con valores iniciales
"""
# syntax
tpl = ("item1", "item2", "item3")
"""
fruits = ("banana", "orange", "mango", "lemon")

# longitud de la tupla
"""
Usamos el metodo len() para obtener la longitud de una tupla.
# syntax
tpl = ("item1", "item2", "item3")
len(tpl)
"""

# Acceso a elementos de tupla
"""
* indexacion positiva similar al tipo de datos de lista, usamos indexacion positiva o negativa para acceder a elementos de tupla.

# syntax
tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]
"""
fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# * indexacion negativa la indexacion negativa significa comenzar desde el final, -1 se refiere al ultimo elemento, -2 se refiere al penultimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.
"""
# syntax
tpl = ("item1", "item2", "item3", "item4")
first_item = tpl[-4]
second_item = tpl[-3]
"""
fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# rebanar tuplas
"""
Podemos dividir una subtupla especificando un rango de indices donde comenzar y donde terminar en la tupla, el valor devuelto sera una nueva tupla con los elementos especificados.
"""
# Rango de indices positivos
"""
# syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]
"""
fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]

# Rango de indices negativos
# syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]

# Cambiar tuplas a listas
"""
Podemos cambiar tuplas por listas y listas por tuplas es inmutable si queremos modificar una tupla debemos cambiarla a una lista.
# syntax
tpl = ("item1", "item2", "item3", "item4")
lst = list(tpl)
"""
fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Comprobacion de un elemento en una tupla
"""
Podemos verificar si un elemento existe o no en una tupla usando in, devuelve un valor booleano.
# syntax
tpl = ("item1", "item2", "item3", "item4")
"item2" in tpl
"""
fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)
print("apple" in fruits)
fruits[0] = "apple"

# Union de tuplas
"""
Podemos unir dos o mas tuplas usando el operador +
# syntax
tpl1 = ("item1", "item2", "item3")
tpl2 = ("item4", "item5", "item6")
tpl3 = tpl1 + tpl2
"""
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables

# Eliminacion de tuplas
"""
No es posible eliminar un solo elemento en una tupla, pero posible eliminar la tupla en si usando del.
# syntax
tpl1 = ("item1", "item2", "item3")
del tpl1
"""
fruits = ("banana", "orange", "mango", "lemon")
del fruits