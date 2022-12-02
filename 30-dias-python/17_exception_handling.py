# Exception Handling
# Manejo de excepciones
"""
Python usa try y except para manejar los errores con gracia.
Una salida elegante (o manejo elegante) de errores es un lenguaje de programacion simple: un programa detecta una condicion de eeror grave y, como resultado, "sale con gracia", de manera controlada. A menudo, el programa imprime un mensaje de error descriptivo en un terminal o registro como parte de la salida ordenada, esto hace que nuestra aplicacion sea mas robusta. la causa de una excepcion suele ser externa al propio programa. Un ejemplo de excepciones podria ser una entrada incorrecta, un nombre de archivo incorrecto, no poder encontrar un archivo incorrecta, un nombre de archivo incorrecto, no poder encontrar un archivo, un dispositivo IO que no funciona correctamente. El manejo elegante de los errores evita que nuestra aplicaciones se bloqueen.
Hemos cubierto los diferentes tipos de errores de python en la seccion anterior.
Si usamos try y except en nuestro programa, entonces no generara errores en esos bloques.
"""
"""
try:
  code in this block if things go well
except:
  code in this block run if things go wrong
"""
# Ejemplo:
try:
  print(10 + "5")
except:
  print("Something went wrong")

"""
En el ejemplo anterior, el segundo operando es una cadena. Podriamos cambiarlo a float o int para agregarlo con el numero para que funcione. Pero sin ningun cambio, se ejecutara el segundo bloque, excepto.
"""
# Ejemplo:
try:
  name = input("Enter your name: ")
  year_born = input("Year you were born: ")
  age = 2019 - year_born
  print(f"You are {name}. And your age is {age}.")
except:
  print("Something went wrong")

"""
En el ejemplo anterior, el bloque de excepcion se ejecutara y no conocemos exactamente el problema. Para analizar el problema, podemos usar los diferentes tipos de error con excepcion.
En el siguiente ejemplo, manejara el error y tambien nos dira el tipo de error generado.
"""
try:
  name = input("Enter your name: ")
  year_born = input("Year you were born: ")
  age = 2019 - year_born
  print(f"You are {name}. And your age is {age}.")
except TypeError:
  print("Type error occured")
except ValueError:
  print("Value error occured")
except ZeroDivisionError:
  print("Zero division error occured")

"""
En el codigo anterior, la salida sera TypeError. Ahora, agreguemos un bloque adicional:
"""
try:
  name = input("Enter your name: ")
  year_born = input("Year you born: ")
  age = 2019 - int(year_born)
  print("You are {name}. And your age is {age}.")
except TypeError:
  print("Type error occur")
except ValueError:
  print("Value error occur")
except ZeroDivisionError:
  print("Zero division error occur")
else:
  print("I usually run with the try block")
finally:
  print("I alway run.")

"""
Tambien se acorta el codigo anterior de la siguiente manera:
"""
try:
  name = input("Enter your name: ")
  year_born = input("Year you born: ")
  age = 2019 - int(year_born)
  print("You are {name}. And your age is {age}.")
except Exception as e:
  print(e)

# Empaquetar y desempaquetar argumentos en Python
"""
Usamos dos operadores:
* para tuplas
* para diccionarios
Tomemos como ejemplo a continuacion. Solo necesita argumentos, pero tenemos una lista. Podemos descomprimir la lista y cambiar el argumento.
"""
# Desembalaje
# Lista de desembalaje
def sum_of_five_nums(a, b, c, d, e):
  return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst))

"""
Cuando ejecutamos este codigo, genera un error, porque esta funcion toma numeros (no una lista) como argumentos. Descomprimamos/desestructuramos la lista.
"""
def sum_of_five_nums(a, b, c, d, e):
  return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

"""
Tambien podemos usar el desempaquetado en la funcion incorporada de rango que espera un comienzo y un final.
"""
numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

"""
Una lista o una tupla tambien se pueden descomprimir asi:
"""
countries = ["Peru", "Brasil", "Chile", "Colombia", "Venezuela"]
pe, br, ch, *rest = countries
print(pe, br, ch, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

# Desempaquetar diccionarios
def unpacking_person_info(name, country, city, age):
  return f"{name} lives in {country}, {city}. He is {age} year old."
dct = {"name":"Gustavo", "country":"Peru", "city":"Lima", "age":25}
print(unpacking_person_info(**dct))

# Embalaje
"""
A veces, nunca sabemos cuantos argumentos se deben pasar a una funcion de Python. Podemos usar el metodo de empaquetamiento para permitir que nuestra funcion tome un numero ilimitado o un numero arbitrario de argumentos.
"""
# Listas de embalaje
def sum_all(*args):
  s = 0
  for i in args:
    s += i
  return s
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Diccionarios de embalaje
def packing_person_info(**kwargs):
  # check the type of kwargs and it is a dict type
  # print(type(kwargs))
  # printing dictionary items
  for key in kwargs:
    print("{key} = {kwargs[key]}")
  return kwargs
print(packing_person_info(name = "Gustavo", country = "Peru", city = "Lima", age = 20))

# Difundir en Python
"""
Al igual que en javaScript, la propagacion es posible en Python.
Comprobemoslo en un ejemplo a continuacion:
"""
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ["Peru", "Colombia", "Brasil"]
country_lst_two = ["Chile", "Mexico"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerar
"""
Si estamos interesados en el indice de un lista, usamos la funcion integrada de enumeracion para obtener el indice de cada elemento de la lista.
"""
for index, item in enumerate([20, 30, 40]):
  print(index, item)

for index, i in enumerate(countries):
  print("hi")
  if i == "Peru":
    print("The country {i} has been found at index {index}")

# Zip (Cremallera)
"""
A veces nos gustaria combinar listas al recorrerlas
"""
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
  fruits_and_veges.append({"fruit":f, "veg":v})
print(fruits_and_veges)