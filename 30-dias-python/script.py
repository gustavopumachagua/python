import sys
print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2]))

# Algunos comando de sistema utiles:
# to exit sys
# sys.exit()
# to know the largest integer variable it takes
sys.maxsize
# to know environment path
sys.path
# to know the version of python you are using
sys.version

# Modulo de estadisticas
"""
El modulo de estadisticas proporciona funciones para estadisticas matematicas de datos numericos.
Las funciones estadisticas populares que se definen en este modulo: media, mediana, moda, desviacion estandar, etc.
"""
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Modulo Matematico
"""
Modulo que contiene muchas operaciones matematicas y constantes.
"""
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

"""
Ahora, hemos importado el modulo matematico que contiene muchas funciones que pueden ayudarnos a realizar calculos matematicos. Para verificar que funciones tiene el modulo, podemos usar help(math) o dir(math).
Esto mostrara las funciones disponibles en el modulo. Si queremos importar solo una funcion especifica del modulo, la importamos de la siguiente manera:
"""
from math import pi
print(pi)
# Tambien es posible importar multiples funciones a la vez

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)
print(sqrt(2))
print(pow(2, 3))
print(floor(9.81))
print(ceil(9.81))
print(math.log10(100))

"""
Pero si queremos importar todas las funciones en el modulo matematico, podemos usar *.
"""
from math import *
print(pi)
print(sqrt(2))
print(pow(2, 3))
print(floor(9.81))
print(ceil(9.81))
print(math.log10(100))

# Cuando importamos tambien podemos renombrar el nombre de la funcion.
from math import pi as PI
print(PI)

# Modulo de cadena
"""
Un modulo de cadena es un modulo util para muchos propositos.
El siguiente ejemplo muestra algunos usos del modulo de cadena.
"""
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# Modulo aleatorio
"""
A estas alturas ya esta familiarizado con la importacion de modulos. Hagamos una importacion mas para familiarizarnos con ella. Importemos un modulo aleatorio que nos da un numero aleatorio entre 0 y 0.9999999..... El modulo aleatorio tiene muchas funciones, pero en esta seccion solo usaremos random y randint.
"""
from random import random, randint
print(random())
print(randint(5, 20))