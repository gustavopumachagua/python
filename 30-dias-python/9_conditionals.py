# conditionals
"""
De forma predeterminada, las declaraciones en el script de Python se ejecutan secuencialmente de arriba a abajo. Si la logica de procesamiento lo requiere, el flujo secuencial de ejecucion se puede alterar de dos formas:
* Ejecucion condicional: se ejecutara un bloque de una o mas sentencias si cierta expresion es verdadera
* Ejecucion repetitiva: un bloque de una o mas sentencias se ejecutara de forma repetitiva siempre que cierta expresion sea verdadera. En esta seccion, cubriremos las declaraciones if, else y elif.
Los operadores logicos y de comparacion que aprendimos en las secciones anteriores seran utiles aqui.
"""
# If Condition
"""
En Python y otros lenguajes de programacion, la palabra clave if se usa para verificar si una condicion es verdadera y ejecutar el codigo de bloque. Recuerde la sangria despues de los dos puntos.
"""
# syntax
"""
if condition:
this part of code runs for truthy conditions
"""

# Ejemplo 1
"""
a = 3
if a > 0:
  print("A is a positive number")
# A is a positive number
"""
"""
Como puede ver en el ejemplo anterior, 3 es mayor que 0.
La condicion era verdadera y se ejecuto el codigo de bloque.
Sin embargo, si la condicion es falsa, no vemos el resultado.
Para ver el resultado de la condicion falsa, deberiamos tener otro bloque, que va a ser else.
"""

# If Else
"""
Si la condicion es verdadera, que ejecutara el primer bloque, si no, se jecutara la otra condicion.

# syntax
if condition:
  this part of code runs for truthy conditions
else:
  this part of code runs for false conditions
"""

# ejemplo
a = 3
if a < 0:
  print("A is a negative number")
else:
  print("A is a positive number")

"""
La condicion anterior resulta falsa, por lo que se ejecuto el bloque else. ¿Que tal si nuestra condicion es mas de dos?
Podriamos usar _elif_.
"""

# If Elif Else
"""
En nuestra vida diaria, tomamos decisiones a diario. Tomamos decisiones no comprobando una o dos condiciones, sino multiples condiciones.
Al igual que la vida, la programacion tambien esta llena de condiciones. Usamos elif cuando tenemos multiples condiciones.

# syntax
if condition:
  code
elif condition:
  code
else:
  code
"""

# ejemplo
a = 0
if a > 0:
  print("A is a positive number")
elif a < 0:
  print("A is a negative numbers")
else:
  print("A is zero")

# Short Hand
"""
# syntax
code if condition else code
"""

# ejemplo
a = 3
print("A is positive") if a > 0 else print("A is negative")

# Nested Conditions
"""
Las condiciones se pueden anidar
# syntax
if condition:
  code
  if condition:
  code
"""

# Ejemplo:
a = 0
if a > 0:
  if a % 2 == 0:
    print("A is a positive and even integer")
  else:
    print("A is a positive number")
elif a == 0:
  print("A is zero")
else:
  print("A is a negative number")
"""
Podemos evitar escribir condiciones anidadas usando el operador logico and.
"""
# If Condition and Logical Operators
"""
# syntax
if condition and condition:
  code
"""
# ejemplo:
a = 0
if a > 0 and a % 2 == 0:
  print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
  print("A is a positive integer")
elif a == 0:
  print("A is zero")
else:
  print("A is negative")

# Operadores logicos si y o
"""
# syntax
if condition or condition:
  code
"""
# Ejemplo:
user = "Gustavo"
access_level = 3
if user == "admin" or access_level >= 4:
  print("Access granted!")
else:
  print("Access denied!")