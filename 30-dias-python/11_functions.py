# Functions
"""
Hasta ahora hemos visto muchas funciones integradas de Python. En esta seccion, nos centraremos en las funciones personalizadas. ¿Que es una funcion?
Antes de comenzar a crear funciones, aprendamos que es una funcion y por que las necesitamos.
"""
# Definicion de una funcion
"""
Una funcion es un bloque reutilizable de codigo o declaraciones de programacion diseñadas para realizar una determinada tarea. Para definir o declarar una funcion, Python proporciona la palabra clave def.
La siguiente es la sintaxis para definir una funcion. El bloque de funcion de codigo se ejecuta solo si se llama o invoca la funcion.
"""
# Declarar y llamar a una funcion
"""
Cuando hacemos una funcion, la llamamos declarando una funcion. Cuando comenzamos a usar it, lo llamamos llamar o invocar una funcion.
La funcion se puede declarar con o sin parametros.

# syntax
# Declaring a function
def function_name():
  codes
  codes
# Calling a function
function_name()
"""
# Funcion sin parametros
"""
La funcion se puede declarar sin parametros.
"""
#Ejemplo:
def generate_full_name ():
  first_name = "Gustavo"
  last_name = "Pumachagua"
  space = " "
  full_name = first_name + space + last_name
  print(full_name)
generate_full_name()

def add_two_numbers ():
  num_one = 2
  num_two = 3
  total = num_one + num_two
  print(total)
add_two_numbers()

# Funcion que devuelve un valor - parte 1
"""
La funcion tambien puede devolver valores, si una funcion no tiene una declaracion de devolucion, el valor de la funcion es Ninguno. Reescribamos las funciones anteriores usando return. De ahora en adelante, obtenemos un valor de una funcion cuando llamamos a la funcion y la imprimimos.
"""
def generate_full_name ():
  first_name = "Gustavo"
  last_name = "Pumachagua"
  space = " "
  full_name = first_name + space +last_name
  return full_name
print(generate_full_name())

def add_two_numbers ():
  num_one = 2
  num_two = 3
  total = num_one + num_two
  return total
print(add_two_numbers())

# Funcion con parametros
"""
En una funcion podemos pasar diferentes tipos de datos (numero, cadena, booleano, lista, tupla, diccionario o conjunto) como parametro

* Parametro unico: si nuestra funcion toma un parametro, debemos llamar a nuestra funcion con un argumento

# syntax
# Declaring a function
def function_name(parameter):
  codes
  codes
# Calling function
print(function_name(argument))
"""

# Ejemplo:
def greetings (name):
  message = name + ", welcome to Python for Everyone!"
  return message
print(greetings("Gustavo"))

def add_ten(num):
  ten = 10
  return num + ten
print(add_ten(90))

def square_number(x):
  return x * x
print(square_number(2))

def area_of_circle (r):
  PI = 3.14
  area = PI * r ** 2
  return area
print(area_of_circle(10))

def sum_of_numbers(n):
  total = 0
  for i in range(n+1):
    total+= i
  print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

"""
* Dos parametros: una funcion puede o no tener un parametro o parametros.
Una funcion tambien puede tener dos o mas parametros. Si nuestra funcion toma parametros, deberiamos llamarla con argumentos. Comprobemos una funcion con dos parametros:

# syntax
# Declaring a function
def function_name(para1, para2):
  codes
  codes
# calling function
print(function_name(arg1, arg2))
"""
# Ejemplo:
def generate_full_name (first_name, last_name):
  space = " "
  full_name = first_name + space + last_name
  return full_name
print("Full Name: ", generate_full_name("Gustavo", "Pumachagua"))

def sum_two_numbers (num_one, num_two):
  sum = num_one + num_two
  return sum
print("Sum of two numbers: ", sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
  age = current_year - birth_year
  return age
print("Age: ", calculate_age(2021, 1819))

def weight_of_object(mass, gravity):
  weight = str(mass * gravity) + " N"
  return weight
print("Weight of an object in Newtons: ", weight_of_object(100, 9.81))

# Pasar argumentos con clave y valor
"""
Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

# syntax
# Declaring a function
def function_name(para1, para2):
  codes
  codes
# Calling function
print(fuction_name(para1 = "Gustavo", para2 = "Perez"))
"""
# Ejemplo:
def print_fullname(firstname, lastname):
  space = " "
  full_name = firstname + space + lastname
  print(full_name)
print(print_fullname(firstname = "Gustavo", lastname = "Pumachagua"))

def add_two_numbers (num1, num2):
  total = num1 + num2
  print(total)
print(add_two_numbers(num2 = 3, num1 = 2))

# Funcion que devuelve un valor - Parte 2
"""
Si no devolvemos un valor con una funcion, entonces nuestra funcion devuelve Ninguno de forma predeterminada. Para devolver un valor con una funcion usamos la palabra clave return seguida de la variable que estamos devolviendo.
Podemos devolver cualquier tipo de tipo de datos de una funcion.
"""
# Devolver una cadena: Ejemplo

def print_name(firstname):
  return firstname
print_name("Gustavo")

def print_full_name(firstname, lastname):
  space = " "
  full_name = firstname + space + lastname
  return full_name
print_full_name(firstname = "Gustavo", lastname = "Pumachagua")

# Devolviendo un numero:
# Ejemplo:
def add_two_numbers (num1, num2):
  total = num1 + num2
  return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
  age = current_year - birth_year
  return age
print("Age: ", calculate_age(2019, 1819))

# * Devolver un valor booleano: Ejemplo:
def is_even (n):
  if n % 2 == 0:
    print("even")
    return True
  return False
print(is_even(10))
print(is_even(7))

# Devolver una lista: Ejemplo:
def find_even_numbers(n):
  evens = []
  for i in range(n + 1):
    if i % 2 == 0:
      evens.append(i)
  return evens
print(find_even_numbers(10))

# Funcion con parametros predeterminados
"""
A veces pasamos valores predeterminados a los parametros, cuando invocamos la funcion.
Si no pasamos argumentos al llamar a la funcion, se utilizaran sus valores predeterminados.

# syntax
# Declaring a function
def function_name(param = value):
  codes
  codes
# Calling function
function_name()
function_name(arg)
"""
# Ejemplo:
def greetings (name = "Gustavo"):
  message = name + ", welcome to python for Everyone!"
  return message
print(greetings())
print(greetings("Ruben"))

def generate_full_name (first_name = "Ruben", last_name = "Pumachagua"):
  space = " "
  full_name = first_name + space + last_name
  return full_name
print(generate_full_name())
print(generate_full_name("Pedro", "Vertiz"))

def calculate_age (birth_year, current_year = 2021):
  age = current_year - birth_year
  return age
print("Age: ", calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
  weight = str(mass * gravity) + "N"
  return weight
print("Weight of an object in Newtons: ", weight_of_object(100))
print("Weight of an object in Newtons: ", weight_of_object(100, 1.62))

# Numero arbitrario de argumentos
"""
Si no conocemos la cantidad de argumentos que le pasamos a nuestra funcion, podemos crear una funcion que pueda tomar una cantidad arbitraria de argumentos agregando * antes del nombre del parametro.

# syntax
# Declaring a function
def function_name(*args):
  codes
  codes
# Calling function
function_name(param1, param2, param3,.....)
"""
# Ejemplo:
def sum_all_nums(*nums):
  total = 0
  for num in nums:
    total += num
  return total
print(sum_all_nums(2, 3, 5))

# Numero predeterminado y arbitrario de parametros en funciones

def generate_groups (team, *args):
  print(team)
  for i in args:
    print(i)
print(generate_groups("Team-1", "Gustavo", "Pedro", "Juan", "Luis"))

# Funcion como parametro de otra funcion

# You can pass functions around as parameters
def square_number (n):
  return n * n
def do_something(f, x):
  return f(x)
print(do_something(square_number, 3))