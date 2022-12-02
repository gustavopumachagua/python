# esto es un comentario
"""
esto es un
comentario de
varias lineas.
"""

# Tipos de Datos
# -Numero
"""
* Numeros entero: Numeros enteros (negativo, cero y positivo) Ejemplo:........ -3, -2, -1, 0, 1, 2, 3.......
* Flotante: Numero decimal Ejemplo: ........ -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ............
* Complejo: 1 + j, 2 + 4j
"""
# - String
"""
Una coleccion de uno o mas caracteres bajo comillas simple o dobles. Si una cadena es mas de una oracion, usamos una comilla triple.
Ejemplo:
"""
"Asabeneh"
"Finland"
"Python"
"I love teaching"
"I hope you are enjoying the first day of 30DaysOfPython Challenge"
# - Booleanos
"""
Un tipo de datos booleano es un valor verdadero o falso. T y F deben estar siempre en mayusculas.
Ejemplo:
"""
True # Is the light on? If it is on, then the value is True.
False # Is the light on? If, the values is False.
# - Lista
"""
La lista de Python es una coleccion ordenada que permite almacenar diferentes tipos de elementos de datos. Una lista es similar a una matriz en javaScript.
Ejemplo:
"""
[0, 1, 2, 3, 4, 5] # all are the same data types - a list of numbers.
["Banana", "Orange", "Mango", "Avocado"] # all the same data types - a list of strings (fruits).
["Finland", "Estonia", "Sweden", "Norway"] # all the same data types - a list of strings (countries).
["Banana", 10, False, 9.81] # different data types in the list - string, integer, boolean and float.
# - Diccionario
"""
Un objeto de diccionario de python es una coleccion desordenada de datos en un formato de par de valores clave.
Ejemplo:
"""
{
  "first_name": "Gustavo",
  "last_name" : "Pumachagua",
  "country" : "Peru",
  "age" : 25,
  "is_married" : True,
  "skills" : ["JS", "React", "NodeJS", "Python"]
}
# - Tupla
"""
Una tupla es una coleccion ordenada de diferentes tipos de datos como una lista, pero las tuplas no se pueden modificar una vez que se crean.
Son inmutables
Ejemplo:
"""
("Gustavo", "Raul", "Maria", "Cesar", "Juan") # Names
("Earth", "Jupiter", "Neptune", "Mars", "Venus", "Saturn", "Uranus", "Mercury") # Planets
# - Set
"""
Un conjunto es una coleccion de tipos de datos similar a una lista y una tupla. A diferencia de list y tupla, set no es una coleccion ordenada de elementos. Al igual que en Matematicas, la configuracion en Python almacena solo elementos unicos.
En secciones posteriores, entraremos en detalle sobre todos y cada uno de los tipos de datos de Python.
Ejemplo:
"""
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set

# Comprobacion de tipos de datos
"""
Para verificar el tipo de datos de ciertos datos/variables, usamos la funcion de tipo
"""
print(2 + 3)      # addition (+)
print( 3 - 1)     # subtraction (-)
print(2 * 3)      # multiplication (*)
print(3 / 2)      # division (/)
print(3 ** 2)     # exponential (**)
print(3 % 2)      # modulus (%)
print(3 // 2)     # floor division operator (//)

# Checking data types
print(type(10))      # Int
print(type(3.14))    # Float
print(type(1 + 3j))  # Complex number
print(type("Gustavo")) # String
print(type([1, 2, 3])) # List
print(type({"name" : "Gustavo"})) # Dictionary
print(type({9.8, 3.14, 2.7})) # Set
print(type((9.8, 3.14, 2.7))) # Tuple