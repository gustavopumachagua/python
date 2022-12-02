# Booleano
"""
Un tipo de datos booleano representa uno de los dos valores: True o False. El uso de estos tipos de datos quedara claro una vez que comencemos a usar el operador de comparacion. La primera letra T para Verdadero y F para Falso debe ser mayuscula a diferencia de javaScript.
Ejemplo:
valores booleanos
"""
print(True)
print(False)

# Operadores
"""
El lenguaje Python admite varios tipos de operadores. En esta seccion, nos centraremos en algunos de ellos.
"""

# Operadores de Asignacion
"""
Los operadores de asignacion se utilizan para asignar valores a las variables.
Tomemos = como ejemplo. El signo igual en matematicas muestra que dos valores son iguales, sin embargo, en Python significa que estamos almacenado un valor en una determinada variable y lo llamamos asignacion o asignacion de valor a una variable.
"""
# Operadores aritmeticos:
"""
* Suma (+): a + b
* Resta (-): a - b
* Multiplicacion (*): a * b
* Division (/): a / b
* Modulo (%): a % b
* Division de piso (//): a // b
* Exponenciacion (**): a ** b
Ejemplo: Enteros
"""
# Arithmetic Operations in Python
# Integers
print("Addition: ", 1 + 2)          # 3
print("Subtraction: ", 2 - 1)       # 1
print("Multiplication: ", 2 * 3)    # 6
print("Division: ", 4 / 2)          # 2.0
print("Division: ", 6 / 2)          # 3.0
print("Division: ", 7 / 2)          # 3.5
print("Division without the remainder: ", 7 // 2)     # 3
print("Division without the remainder: ", 7 // 3)     # 2
print("Modulus: ", 3 % 2)           # 1
print("Exponentiation: ", 2 ** 3)   # 8

# Ejemplo: Floats
# Floating numbers
print("Floating Point Number, PI", 3.14)
print("Floating Point Number, gravity", 9.81)

# Ejemplo Numeros Complejos
# Complex numbers
print("Complex number: ", 1 + 1j)
print("Multiplying complex numbers: ", (1 + 1j) * (1 - 1j))

"""
Declaremos una variable y asignemos un tipo de dato numerico. Voy a usar una variable de un solo caracter, pero recuerde que no desarrolle el habito de declarar este tipo de variables. Los nombres de las variables deben ser siempre memotecnicos.
"""
# Ejemplo
# Declaring the variable at the top first
a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type
# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b
# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print("a + b = ", total)
print("a - b = ", diff)
print("a * b = ", product)
print("a / b = ", division)
print("a % b = ", remainder)
print("a // b = ", floor_division)
print("a ** b = ", exponential)

# Ejemplo
print("== Addition, Subtraction, Multiplication, Division, Modulus == ")
# Declaring values and organizing them together
num_one = 3
num_two = 4
# Declaring values and organizing them together
num_one = 3
num_two = 4
# Aritmetic Operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one
# Printing values with label
print("total: ", total)
print("difference: ", diff)
print("product: ", product)
print("division: ", div)
print("remainder: ", remainder)

"""
Empecemos a conectar los puntos y empecemos a hacer uso de lo que ya sabemos para calcular (area, volumen, densidad, peso, perimetro, distancia, fuerza).
Ejemplo:
"""
# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of circle: ", area_of_circle)
# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of rectangle: ", area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, "N")

# Calculate the density of a liquid
mass = 75
volume = 0.075
density = mass / volume

# Operadores de comparacion
"""
En programacion comparamos valores, usamos operadores de comparacion para comparar dos valores.
Comprobamos si un valor es mayor o menor o igual a otro valor.
"""
# Ejemplo: Operadores de comparacion
print(3 > 2)                # True
print(3 >= 2)               # True
print(3 < 2)                # False
print(2 < 3)                # True
print(2 <= 3)               # True
print(3 == 2)               # False
print(3 != 2)               # True
print(len("mango") == len("avocado"))          # False
print(len("mango") != len("avocado"))          # True
print(len("mango") < len("avocado"))           # True
print(len("milk") != len("meat"))              # False
print(len("milk") == len("meat"))              # True
print(len("tomato") == len("potato"))          # True
print(len("python") > len("dragon"))           # False

# Comparing something gives either a True or False
print("True == True: ", True == True)
print("True == False: ", True == False)
print("False == False: ", False == False)

"""
Ademas del operador de comparacion anterior, Python usa:
* is: Devuelve verdadero si ambas variables son el mismo objetivo (x es y)
* is not: Devuelve verdadero si ambas variables no son el mismo objetivo (x no es y)
* in: Devuelve True si la lista consultada contiene un determinado elemento (x en y)
* not in: Devuelve True si la lista consultada no tiene un determinado elemento (x en y)
"""
print("1 is 1", 1 is 1)                    # True
print("1 is not 2", 1 is not 2)            # True
print("A in Gustavo", "A" in "Gustavo")    # True
print("B in Gustavo", "B" in "Gustavo")    # False
print("coding" in "coding for all")        # True
print("a in an: ", "a" in "an")            # True
print("4 is 2 ** 2: ", 4 is 2 ** 2)        # True

# Operadores logicos
"""
A diferencia de otros lenguajes de programacion, Python usa clave y, o y no para los operadores logicos. Los operadores logicos se utilizan para combinar sentencias condicionales:
"""
print(3 > 2 and 4 > 3)           # True
print(3 > 2 and 4 < 3)           # False
print(3 < 2 and 4 < 3)           # False
print("True and True: ", True and True)
print(3 > 2 or 4 > 3)            # True
print(3 > 2 or 4 < 3)            # True
print(3 < 2 or 4 < 3)            # False
print("True or False: ", True or False)
print(not 3 > 2)                 # False
print(not True)                  # False
print(not False)                 # True
print(not not True)              # True
print(not not False)             # False
