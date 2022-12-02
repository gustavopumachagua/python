# Lista de comprension
"""
La comprension de listas en Python es una forma compacta de crear uns lista a partir de una secuencia. Es una forma corta de crear una nueva lista.
La comprension de listas es considerablemente mas rapida que procesar una lista usando el bucle for.

# syntax
[i for i in iterable if expression]
"""
"""
Ejemplo:
Por ejemplo, si deseas cambiar una cadena a una lista de caracteres. Puedes usar un par de metodos. Veamos algunos de ellos:
"""

# One way
language = "Python"
lst = list(language)
print(type(lst))
print(lst)

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

"""
Ejemplo:
Por ejemplo, si deseas generar una lista de numeros
"""
# Generating numbers
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

# It is also possible to make a list of tuples
numbers = [(i, i * i)for i in range(11)]
print(numbers)

# Ejemplo
"""
La comprension de listas se puede combinar con la expresion if
"""

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# Lambda Function
"""
La funcion Lambda es una pequeña funcion anonima sin nombre. Puede tomar cualquier numero de argumentos, pero solo puede tener una expresion.
La funcion lambda es similar a las funciones anonimas en javaScript. Lo necesitamos cuando queremos escribir una funcion anonima dentro de otra funcion.
"""
# Creacion de una funcion lambda
"""
Para crear una funcion lambda, usamos la palabra clave lambda seguida de un parametro, seguido de una expresion.
Consulte la sintaxis y el ejemplo a continuacion. La funcion lambda no usa return pero devuelve explicitamente la expresion.
"""
"""
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
"""
# Ejemplo:
# Named function
def add_two_nums(a, b):
  return a + b
print(add_two_nums(2, 3))

# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))

# self invoking lambda function
(lambda a, b: a + b)(2, 3)

square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 -3 * b + 4 * c
print(multiple_variable(5, 5, 3))

# Funcion lambda dentro de otra funcion
# Usar una funcion lambda dentro de otra funcion.
def power(x):
  return lambda n : x ** n
cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)