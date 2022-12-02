# Bucles
"""
La vida esta llena de rutinas. En programacion tambien hacemos muchas tareas repetitivas.
Para manejar tareas repetitivas, los lenguajes de programacion usan bucles. El lenguaje de programacion Python tambien proporciona los siguientes tipos de dos bucles:
* while loop
* for loop
"""
# While Loop
"""
Usamos la palabra reservada while para hacer un bucle while. Se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condicion dada. Cuando la condicion se vuelve falsa, las lineas de codigo despues del ciclo continuaran ejecutandose.
"""
"""
# syntax
while condition:
  code goes here
"""
# Ejemplo:
count = 0
while count < 5:
  print(count)
  count = count + 1

"""
En el ciclo while anterior, la condicion se vuelve falsa cuando el conteo es 5. Ahi es cuando el ciclo se detiene.
Si estamos interesados en ejecutar un bloque de codigo una vez que la condicion ya no sea cierta, podemos usar else.
"""
"""
# syntax
while condition:
  code goes here
else:
  code goes here
"""

# ejemplo:
count = 0
while count < 5:
  print(count)
  count = count + 1
else:
  print(count)

"""
La condicion del ciclo anterior sera falsa cuando el conteo sea 5 y el ciclo se detenga y la ejecucion inicie la instruccion else. Como resultado se imprimiria 5.
"""
# Break and Continue - Part 1
"""
* Break: Usamos break cuando queremos salir o detener el bucle.

# syntax
while condition:
  code goes here
  if another_condition:
    break
"""

# Ejemplo:
count = 0
while count < 5:
  print(count)
  count = count + 1
  if count == 3:
    break

"""
El ciclo while anterior solo imprime 0, 1, 2, pero cuando llega a 3 se detiene.
* Continue: Con la instruccion continuar podemos omitir la iteracion actual y continuar con la siguiente:

# syntax
while condition:
  code goes here
  if another_condition:
    continue
"""
# Ejemplo:
count = 0
while count < 5:
  if count == 3:
    continue
  print(count)
  count = count + 1

"""
El ciclo while anterior solo imprime 0, 1, 2 y 4 ( se salta 3).
"""
# For Loop
"""
Una palabra clave for se usa para hacer un bucle for, similar a otros lenguajes de programacion, pero con algunas diferencias de sintaxis. Loop se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).
"""
"""
* For loop with list

# syntax
for iterator in lst:
  code goes here
"""
# ejemplo:
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
  print(number)

# For loop with string
"""
# syntax
for iterator in string:
  code goes here
"""
# Ejemplo:
language = "Python"
for letter in language:
  print(letter)

for i in range(len(language)):
  print(language[i])

# For loop with tuple
"""
# syntax
for iterator in tpl:
  code goes here
"""

# Ejemplo:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
  print(number)

"""
* For loop con diccionario hacer un bucle a traves de un diccionario le da la clave del diccionario.

# syntax
for iterator in dct:
  code goes here
"""
# Ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":22,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street":"Space street",
    "zipcode":"02210"
  }
}
for key in person:
  print(key)
for key, value in person.items():
  print(key, value)

"""
* Loops in set

# syntax
for iterator in st:
  code goes here
"""
# Ejemplo:
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
  print(company)

# Break and Continue - Part 2
"""
Breve recordatorio: Break: Usamos break cuando queremos detener nuestro ciclo antes de que se complete.

# syntax

for iterator in sequence:
  code goes here
  if condition:
    break
"""

# Ejemplo:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
  print(number)
  if number == 3:
    break

"""
En el ejemplo anterior, el bucle se detiene cuando llega a 3.
Continuar: usamos continuar cuando nos gusta saltarnos algunos de los pasos en la iteracion del bucle.

# syntax
for iterator in sequence:
  code goes here
  if condition:
    continue
"""

# Ejemplo:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
  print(number)
  if number == 3:
    continue
  print("Next number should be ", number + 1) if number != 5 else print("loop's end")
print("outside the loop")

"""
En el ejemplo anterior, si el numero es igual a 3, se omite el paso posterior a la condicion (pero dentro del ciclo) y la ejecucion del ciclo continua si quedan iterciones.
"""

# The Range Function
"""
La funcion range() se utiliza como lista de numeros. El range (inicio, fin, paso) toma tres parametros: inicio, fin e incremento. De forma predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (fin). Creando secuencias usando rango.
"""
lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)

lst = list(range(0, 11, 2))
print(lst)
st = set(range(0, 11, 2))
print(st)

"""
# syntax
for iterator in range(start, end, step):
"""

# Ejemplo:
for number in range(11):
  print(number)

"""
Bucle for anidado
"""
"""
Podemos escribir bucles dentro de un bucle.
# syntax
for x in y:
  for t in x:
    print(t)
"""
# Ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":25,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street":"Space street",
    "zipcode":"02210"
  }
}
for key in person:
  if key == "skills":
    for skill in person["skills"]:
      print(skill)

# For Else
"""
si queremos ejecutar algun mensaje cuando finaliza el ciclo, usamos else.

# syntax
for iterator in range(start, end, step):
  do something
else:
  print("The loop ended")
"""
# Ejemplo:
for number in range(11):
  print(number)
else:
  print("The loop stops at", number)

# Pass
"""
En Python, cuando se requiere una declaracion (despues del punto y coma), pero no nos gusta ejecutar ningun codigo alli, podemos escribir la palabra pass para evitar errores. Tambien podemos usarlo como marcador de posicion, para declaraciones futuras.
"""
# Ejemplo:
for number in range(6):
  pass