# Funciones integradas
"""
En Python tenemos muchas funciones integradas. La funciones integradas estan disponibles globalmente para su uso, lo que significa que puede hacer uso de las funciones integradas sin importarlas ni configurarlas. Algunas de las funciones integradas de Python mas utilizadas son las siguientes:
print(), len(), type(), int(), float(), str(), input(), list(), min(), max(), sum(), sorted(), open(), file(), help() y dir().
"""
# Variables
"""
Las variables almacenan datos en la memoria de una computadora. Se recomienda el uso de variables memotecnicas en muchos lenguajes de programacion. Una variable memotecnics es un nombre de variable que se puede recordar y asociar facilmente. Una variable se refiere a una direccion de memoria en la que se almacenan los datos. Numero al principio, caracter especial, guin no estan permitidos al nombrar una variable. Una variable puede tener un nombre corto ( como x, y, z), pero se recomienda enfaticamente un nombre mas descriptivo ( nombre, apellido, edad, pais).
Reglas de nombre de variables de Python
* Un nombre de variable debe comenzar con una letra o el caracter de subrayado
* Un nombre de variable solo puede contener caracteres alfanumericos y guiones bajo (Az, 0-9 y _)
* Los nombres de las variables distinguen entre mayusculas y minusculas (firstname,Firstname, FirstName y FIRSTNAME) son variables diferentes
Veamos nombres de variables validos
"""
"""
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
"""
# Nombres de variables no validos
"""
first-name
first@name
first$name
num-1
1num
"""
"""
Usaremos el estilo estandar de nomenclatura de variables de python que ha sido adoptado por muchos desarrolladores de Python. Los desarrolladores de Python usan la convencion de nomenclatura de variables de caja de serpiente (snake_case).
Usamos un caracter de subrayado despues de cada palabra para una variable que contiene mas de una palabra (ej.. nombre, apellido, velocidad de rotacion del motor). El siguiente ejemplo es un ejemplo de nomenclatura estandar de variables, se requiere guion bajo cuando el nombre de la variable es mas de una palabra.
Cuando asignamos un determinado tipo de datos a una variable, se llama declaracion de variable. Por ejemplo, en el siguiente ejemplo, mi nombre se asigna a una variable first_name. El signo igual es un operador de asignacion.
Asignar significa almacenar datos en la variable. El signo igual en Python no es la igualdad como en Matematicas.
Ejemplo:
"""
# Variables in Python
first_name = "Gustavo"
last_name = "Pumachagua"
country = "Peru"
city = "Lima"
age = 20
is_married = True
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
  "firstname" : "Gustavo",
  "lastname" : "Pumachagua",
  "country" : "Peru",
  "city" : "Lima"
}
"""
Usemos las funciones integradas print() y len().
La funcion de impresion toma un numero ilimitado de argumentos. Un argumento es un valor que se puede pasar o poner dentro del parentesis de la funcion, vea el ejemplo a continuacion.
Ejemplo:
"""
print("Hello, World!") # The text Hello, World! is an argument
print("Hello", ",", "World", "!") # it can take multiple arguments, four arguments have been passed
print(len("Hello, World!")) # it takes only one argument
"""
Imprimamos y tambien encontremos la longitud de las variables declaradas en la parte superior:
Ejemplo:
"""
# Printing the values stored in the variables
print("First name: ", first_name)
print("First name length: ", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

# Declarar multiples variables en una linea
"""
Tambien se pueden declarar multiples variables en una linea:
Ejemplo:
"""
first_name, last_name, country, age, is_married = "Gustavo", "Pumachagua", "Peru", 25, True
print(first_name, last_name, country, age, is_married)
print("First name: ", first_name)
print("Last name: ", last_name)
print("Country: ", country)
print("Age: ", age)
print("Married: ", is_married)

"""
Obtener la entrada del usuario usando la funcion incorporada input().
Asignemos los datos que obtenemos de un usuario a las variables first_name y age
Ejemplo:
"""
first_name = input("What is your name: ")
age = input("How old are you?")
print(first_name)
print(age)

# Tipos de datos
"""
Hay varios tipos de datos en Python. Para identificar el tipo de datos, usamos la funcion incorporada de tipo. Me gustaria pedirle que se concentre en comprender muy bien los diferentes tipos de datos. Cuando se trata de programacion, se trata de tipos de datos. Introduje los tipos de datos desde el principio y viene de nuevo, porque todos los temas estan relacionaos con los tipos de datos. Cubriremos los tipos de datos con mas detalle en sus respectivas secciones.
"""
# Comprobacion de tipos de datos y conversion
"""
Verificar tipos de datos: para verificar el tipo de datos de ciertos datos/variables, usamos el tipo
Ejemplo:
"""
# Different Python data types
# Let's declare variables with various data types
first_name = "Gustavo"           # str
last_name = "Perez"              # str
country = "Peru"                 # str
city = "Lima"                    # str
age = 25                         # int, it is my real age, don't worry about it

# Printing out types
print(type("Gustavo"))            # str
print(type(first_name))           # str
print(type(10))                   # int
print(type(3.14))                 # float
print(type(1 + 1j))               # complex
print(type(True))                 # bool
print(type([1, 2, 3, 4]))         # list
print(type({"name" : "Gustavo", "age" : 20, "is_married": True}))                           # dict
print(type((1, 2)))               # tuple
print(type(zip([1, 2], [3, 4])))  # set
"""
Cating: convertir un tipo de datos a otro tipo de datos. Usamos int(), float(), str(), list, set
Cuando hacemos operaciones aritmeticas, los numeros de cadena deben convertirse primero a int o float; de lo contrario, devolvera un error. Si concatenamos un numero con una cadena, el numero debe convertirse primero en una cadena. Hablaremos sobre la concatenacion en la seccion String.
Ejemplo:
"""
# int to float
num_int = 10
print("num_int", num_int)               # 10
num_float = float(num_int)
print("num_float: ", num_float)         # 10.0

# float to int
gravity = 9.81
print(int(gravity))                     # 9

# int to str
num_int = 10
print(num_int)                          # 10
num_str = str(num_int)
print(num_str)                          # "10"

# str to int or float
num_str = "10.6"
print("num_int", int(num_str))          # 10
print("num_float", float(num_str))      # 10.6

# str to list
first_name = "Ruben"
print(first_name)                       # "Ruben"
first_name_to_list = list(first_name)
print(first_name_to_list)               # ["R", "u", "b", "e", "n"]