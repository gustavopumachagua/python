# Higher Order Functions
"""
En Python, las funciones se tratan como ciudadanos de primera clase, lo que le permite realizar las siguientes operaciones en las funciones:
* Una funcion puede tomar una o mas funciones como parametros
* Una funcion puede ser devuelta como resultado de otra funcion.
* Se puede modificar una funcion
* Se puede asignar una funcion a una variable
En esta seccion, cubriremos:
1. Manejo de funciones como parametros
2. Devolver funciones como valor de retorno de otras funciones
3. Uso de cierres y decoradores de Python
"""
# Funcion como parametro

def sum_numbers(nums):
  return sum(nums)

def higher_order_function(f, lst):
  summation = f(lst)
  return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

# Funcion como valor de retorno
def square(x):
  return x ** 2

def cube(x):
  return x ** 3

def absolute(x):
  if x >= 0:
    return x
  else:
    return -(x)

def higher_order_function(type):
  if type == "square":
    return square
  elif type == "cube":
    return cube
  elif type == "absolute":
    return absolute

result = higher_order_function("square")
print(result(3))
result = higher_order_function("cube")
print(result(3))
result = higher_order_function("absolute")
print(result(-3))

"""
Puede ver en el ejemplo anterior que la funcion de orden superior esta devolviendo diferentes funciones dependiendo del parametro pasado
"""
# Python Closures
"""
Python permite que una funcion anidada acceda al ambito externo de la funcion envolvente.
Esto se conoce como cierre. Echemos un vistazo a como funcionan los cierres en python. En Python, el cierre se crea anidando una funcion dentro de otra funcion encapsuladora y luego devolviendo la funcion interna. Vea el ejemplo a continuacion.
"""
# Ejemplo:
def add_ten():
  ten = 10
  def add(num):
    return num + ten
  return add
closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# Python Decorators
"""
Un decorador es un patron de diseño en Python que permite a un usuario agregar una nueva funcionalidad a un objeto existente sin modificar su estructura.
Los decoradores generalmente se llaman antes de la definicion de una funcion que desea decorar.
"""
# Crear decoradores
"""
Para crear una funcion decoradora, necesitamos una funcion externa con una funcion contenedora interna.
"""
# Ejemplo:
# Normal function
def greeting():
  return "Welcome to Python"
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
g = uppercase_decorator(greeting)
print(g())

# Let us implement the example above with a decorator
"""
This decorator function is a higher order function
that takes a function as a parameter
"""
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
@uppercase_decorator
def greeting():
  return "welcome to python"
print(greeting())

# Aplicar multiples decoradores a una sola funcion
"""
These decorator function are higher order functions that take functions as parameters
"""
# First Decorator
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper

# second decorator
def split_string_decorator(function):
  def wrapper():
    func = function()
    splitted_string = func.split()
    return splitted_string
  return wrapper
@split_string_decorator
@uppercase_decorator
def greeting():
  return "Welcome to Python"
print(greeting())

# Aceptar parametros en funciones de decorador
"""
La mayoria de las veces necesitamos que nuestras funciones tomen parametros, por lo que es posible que debamos definir un decorador que acepte parametros.
"""
def decorator_with_parameters(function):
  def wrapper_accepting_parameters(para1, para2, para3):
    function(para1, para2, para3)
    print("I live in {}".format(para3))
  return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
  print("I am {} {}. I love to teach.".format(first_name, last_name, country))

print_full_name("Gustavo", "Pumachagua", "Peru")

# Funciones integradas de orden superior
"""
Algunas de las funciones integradas de orden superior que cubrimos en esta parte son map(), filter y reduce. La funcion lambda se puede pasar como un parametro y el mejor caso de uso de las funciones lambda es en funciones como mapa, filtro y reduccion.
"""
# Python - Map Function
"""
La funcion map() es una funcion integrada que toma una funcion y es iterable como parametros.

# syntax
map(function, iterable)
"""
# Ejemplo:
numbers = [1, 2, 3, 4, 5]
def square(x):
  return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

# Ejemplo:
numbers_str = ["1", "2", "3", "4", "5"]
numbers_int = map(int, numbers_str)
print(list(numbers_int))

# Ejemplo:
names = ["Gustavo", "Ruben", "Luis", "Cesar"]
def change_to_upper(name):
  return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

"""
Lo que realmente hace el mapa es iterar sobre una lista. Por ejemplo, cambia los nombres a mayusculas y devuelve una nueva lista.
"""
# Python - Filter Function
"""
La funcion filter() llama a la funcion especificada que devuelve un valor booleano para cada elemento de la iterable (lista) especificada. Filtra los elementos que cumplen los criterios de filtrado.

# syntax
filter(function, iterable)
"""

# Ejemplo:
# Lets filter only even numbers
numbers = [1, 2, 3, 4, 5]
def is_even(num):
  if num % 2 == 0:
    return True
  return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# Ejemplo:
numbers = [1, 2, 3, 4, 5]
def is_odd(num):
  if num % 2 != 0:
    return True
  return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

# Filter long name
names = ["Gustavo", "Maria", "Juan", "Luz"]
def is_name_long(name):
  if len(name) > 5:
    return True
  return False
long_names = filter(is_name_long, names)
print(list(long_names))

# Python - Funcion de reduccion
"""
La funcion reduce() esta definida en el modulo functools y debemos importarla desde este modulo. Al igual que el mapa y el filtro, toma dos parametros, una funcion y un iterable.
Sin embargo, no devuelve otro iterable, sino un solo valor.
"""
# Ejemplo:
import functools

numbers_str = ["1", "2", "3", "4", "5"]
def add_two_nums(x, y):
  return int(x) + int(y)
total = functools.reduce(add_two_nums, numbers_str)
print(total)