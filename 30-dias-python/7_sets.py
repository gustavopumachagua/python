# sets
"""
El conjunto es una coleccion de elementos. Dejame llevarte de regreso a tu leccion de Matematicas de primaria o secundaria.
La definicion matematica de un conjunto tambien se puede aplicar en Python. Conjunto es una coleccion de elementos distintos desordenados y no indexados. En Python, el conjunto se usa para almacenar elementos unicos, y es posible encontrar la union, la interseccion, la diferencia simetrica, el subconjunto, el superconjunto y el conjunto disjunto entre conjuntos.
"""
# Crear un conjunto
"""
Usamos corchetes, {} para crear un conjunto o la funcion integrada set().
* Crear un conjunto vacio
# syntax
st = {}
# or
st = set()
"""
# * Creacion de un conjunto con elementos iniciales
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
EJEMPLO:
"""
# syntax
fruits = {"banana", "orange", "mango", "lemon"}

# Obtener la longitud del conjunto
"""
Usamos el metodo len() para encontrar la longitud de un conjunto.
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
len(set)
# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
len(fruits)

# Acceder a elementos en un conjunto
"""
Usamos bucles para acceder a los elementos. Veremos esto en la seccion de bucle.
"""
# Comprobacion de un articulo
"""
Para verificar si existe un elemento en una lista, usamos el operador de membresia.
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
print("Does set st contain item3?", "item3" in st)
# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
print("mango" in fruits)

# Adicion de elementos a un conjunto
"""
Una vez que se crea un conjunto, no podemos cambiar ningun elemento y tambien podemos agregar elementos adicionales.
* Agrega un elemento usando add()
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
st.add("item5")

# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
"""
* Agregar multiples elementos usando update() The update() permite agregar multiples elementos a un conjunto. The update() toma un argumento de lista.
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
st.update(["item5", "item6", "item7"])
# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)

# Eliminacion de elementos de un conjunto
"""
Podemos eliminar un elemento de un conjunto usando el metodo remove(). Si no se encuentra el elemento, el metodo remove() generara errores, por lo que es bueno verificar si el elemento existe en el conjunto dado. Sin embargo, el metodo, discard() no genera ningun error.
"""
# syntax
st = {"item1", "item2", "item3", "item4"}
st.remove("item2")

"""
Los metodos pop() eliminan un elemento aleatorio de una lista y devuelve el elemento eliminado.
"""
# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
fruits.pop()

# Si estamos interesados en el articulo eliminado
fruits = {"banana", "orange", "mango", "lemon"}
removed_item = fruits.pop()

# Borrado de articulos en un conjunto
# Si queremos borrar o vaciar el conjunto, usamos el metodo de limpieza.
# syntax
st = {"item1", "item2", "item3", "item4"}
st.clear()

# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
fruits.clear()
print(fruits)

# Eliminacion de un conjunto
# Si queremos eliminar el conjunto en si, usamos el operador.
# syntax
st = {"item1", "item2", "item3", "item4"}
del st

# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
del fruits

"""
* Convertir lista en conjunto
Podemos convertir lista en conjunto en lista en lista. La conversion de la lista al conjunto elimina los duplicados y solo se reservaran elementos unicos.
"""
# syntax
lst = ["item1", "item2", "item3", "item4", "item1"]
st = set(lst)

# ejemplo:
fruits = ["banana", "orange", "mango", "lemon", "orange", "banana"]
fruits = set(fruits)

# Union de conjuntos
"""
Podemos unir dos conjuntos usando el metodo union() o update().
* Union Este metodo devuelve un nuevo conjunto
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st3 = st1.union(st2)
# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
print(fruits.union(vegetables))

# * Actualizar Este metodo inserta un conjunto en un conjunto dado
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st1.update(st2)

# Ejemplo:
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
fruits.update(vegetables)
print(fruits)

# Busqueda de elementos de interseccion
"""
La interseccion devuelve un conjunto de elementos que estan en ambos conjuntos. Ver el ejemplo
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item3", "item2"}
st1.intersection(st2)
# Ejemplo:
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.intersection(dragon)

# Comprobacion de subconjunto y superconjunto
"""
Un conjunto puede ser un subconjunto o superconjunto de otros conjuntos:
* Subconjunto: issubset()
* Super conjunto: essuperconjunto
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.issubset(st1)
st1.issuperset(st2)

# Ejemplo:
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.issubset(dragon)

# Comprobar la diferencia entre dos conjuntos
"""
Devuelve la diferencia entre dos conjunto.
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.difference(st1)
st1.difference(st2)

# ejempo:
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)

python = {"p", "y", "t", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.difference(dragon)
dragon.difference(python)

# Hallar diferencias simetricas entre dos conjuntos
"""
Devuelve la diferencia simetrica entre dos conjuntos.
Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que estan presentes en ambos conjuntos, matematicamente: (A\B) U (B\A)
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
# it means (A\B) U (B\A)
st2.symmetric_difference(st1)

# Ejemplo:
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.symmetric_difference(dragon)

# Union de conjuntos
"""
Si dos conjuntos no tienen un elementos o elementos comunes, los llamamos conjuntos disjuntos. Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el metodo isdisjoint().
"""
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.isdisjoint(st1)

# Ejemplo:
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python.isdisjoint(dragon)