# Importacion de un modulo
"""
Para importar el archivo usamos la palabra clave de importacion y el nombre del archivo solamente.
"""
# main.py file
import mymodule
print (mymodule.generate_full_name("Gustavo", "Pumachagua"))

# Importar funciones desde un modulo
"""
Podemos tener muchas funciones en un archivo y podemos importar todas las funciones de manera diferente.
"""

# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name("Gustavo", "Pumachagua"))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person["firstname"])

# Importacion de funciones desde un modulo y cambio de nombre
"""
Durante la importacion podemos cambiar el nombre del modulo.
"""
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname("Gustavo", "Pumachagua"))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p["firstname"])

# Import modulos integrados
"""
Al igual que otros lenguajes de programacion, tambien podemos importar modulos importando el archivo/funcion usando la palabra clave import.
importemos el modulo comun que usaremos la mayor parte del tiempo.
Algunos de los modulos incorporados comunes: matematicas, fecha y hora, os, sys, aleatorio, estadisticas, coleccion, json, re
"""
# Modulo del sistema operativo
"""
Usando el modulo python os es posible realizar automaticamente muchas tareas del sistema operativo.
El modulo del sistema operativo en python proporciona funciones para crear, cambiar el directorio de trabajo actual y eliminar un directorio (carpeta), recuperar su contenido, cambiar e identificar el directorio actual.
"""

# import the module
import os
# Creating a directory
os.mkdir("directory_name")
# changing the current directory
os.chdir("path")
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# Modulo del sistema
"""
El modulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecucion de python.
La funcion sys.argv devuelve una lista de argumentos de la linea de comandos pasados a un script de python. El elemento en el indice 0 de esta lista siempre es el nombre del script, en el indice 1 esta el argumento pasado desde la linea de comando.

Ejemplo de un archivo script.py
"""