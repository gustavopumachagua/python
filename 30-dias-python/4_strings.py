# Strings
"""
El texto es un tipo de datos de cadena.
Cualquier tipo de datos escrito como texto es una cadena. Todos los datos entre comillas simples, dobles o triples son cadenas.
Existen diferentes metodos de cadena y funciones integradas para manejar tipos de datos de cadena.
Para verificar la longitud de una cadena, use el metodo len().
"""
# Crear un Strings
letter = "P"
print(letter)
print(len(letter))
greeting = "Hello, World!"
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
"""
La cadena multilinea se crea usando comillas triples simples (''' ''') o triples dobles (""" """).
Consulte el ejemplo a continuacion.
"""
multiline_string = ''' I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
'''
# Another way of doing the same thing
multiline_string = """ I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
"""

# Concatenacion de Strings
"""
Podemos conectar strings juntas. Combinar o conectar Strings se llama concatenacion.
Ejemplo:
"""
first_name = "Gustavo"
last_name = "Pumachagua"
space = " "
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Secuencias de escape en Strings
"""
En Python y otros lenguajes de programacion \ seguido de un caracter es una secuencia de escape.
Veamos los caracteres de escape de escape mas comunes:
* \n: nueva linea
* \t: Tabulador significa (8 espacios)
* \\: barra invertida
* \': Una frase (')
* \": comillas dobles (")
Ahora, veamos el uso de las secuencias de escape anteriores con ejemplos:
"""
print("I hope everyone is enjoying the python challenge. \nAre you ?")
print("Days \tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is backslash symbol (\\)")
print('In every programming language it starts with \" Hello, World!"')
# output
"""
I hope every one is enjoying the Python Challenge.
Are you ?
Days             Topics                Exercises
Day 1               5                     5
Day 2               6                     20
Day 3               5                     23
Day 4               1                     35
This is a backslash symbol (\)
In every programming language it starts with "Hello, World!"
"""

# formato de strings
"""
Formato de cadena de estilo antiguo (% operador)

En Python hay muchas formas de formatear cadenas. En esta seccion, cubriremos algunos de ellos. El operador "%" se utiliza para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con
"especificadores de argumento", simbolos especiales como "%s", "%d", "%f", "%.numero de digitosf".
* %s - Cadena (o cualquier objeto con una representacion de cadena, como numeros)
* %d - Enteros
* %f - Numeros de punto flotante
* "%.number of digitsf" - Numeros de punto flotante con precision fija
"""
# Strings only
first_name = "Gustavo"
last_name = "Perez"
language = "Python"
formated_string = "I am %s %s. I teach %s" %(first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of circle with a radius %s is %.2f." %(radius, area)
python_libraries = ["Django", "Flask", "NumPY", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries: %s" %(python_libraries)
print(formated_string)

# Nuevo formato de cadena de estilo (str.format)
first_name = "Gustavo"
last_name = "Pumachagua"
language = "Python"
formated_string = "I am {} {}. I teach {}".format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
# output
"""
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64
"""
# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of a circle with a radius {} is {:.2f}.".format(radius, area)
print(formated_string)
# Interpolacion de cadenas / cadenas f (Python 3.6+)
"""
Otro nuevo formato de cadena es la interpolacion de cadenas, f-strings. Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.
"""
a = 4
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
# Cadenas de Python como secuencias de caracteres
"""
Las cadenas de Python son secuencias de cracteres y comparten sus metodos basicos de acceso con otras secuencias de objetos ordenadas de Python: listas y tuplas.
La forma mas sencilla de extraer caracteres individuales de cadenas (y miembros individuales de cualquier secuencia) es descomprimirlos en las variables correspondientes.
"""
# Desempaquetar personajes
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Acceso a caracteres en cadenas por indice
"""
En la programacion, el conteo comienza desde cero. Por lo tanto, la primera letra de una cadena tiene un indice cero y la ultima letra de una cadena es la longitud de una cadena menos uno.
"""
language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

"""
Si queremos comenzar desde el extremo derecho, podemos usar la indexacion negativa. -1 es el ultimo indice.
"""
language = "Python"
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Cortar cadenas de Python
"""
En Python podemos dividir cadenas en subcadenas.
"""
language = "Python"
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Invertir una cadena
# Podemos invertir cadenas facilmente en python.
greeting = "Hello, World!"
print(greeting[::-1])

# Saltar caracteres al cortar
"""
Es posible omitir caracteres durante el corte pasando el argumento de paso al metodo de corte.
"""
language = "Python"
pto = language[0:6:2]
print(pto)

# Metodos de cadena
"""
Hay muchos metodos de cadena que nos permiten formatear cadenas. Vea algunos de los metodos de cadena en el siguiente ejemplo:
"""
# capitalize (): convierte el primer caracter de la cadena en letra mayuscula
challenge = "thirty days of python"
print(challenge.capitalize())

# count(): devuelve ocurrencias de subcadena en cadena, cuenta (subcadena, inicio =...., final =....).El inicio es una indexacion inicial para contar y el final es el ultimo indice para contar.
challenge = "thirty days of python"
print(challenge.count("y"))
print(challenge.count("y", 7, 14))
print(challenge.count("th"))

# endswith(): comprueba si una cadena termina con un final especifico
challenge = "thirty days of python"
print(challenge.endswith("on"))
print(challenge.endswith("tion"))

# expandtabs (): reemplaza el caracter de tabulacion con espacios, el tamaño de tabulacion predeterminado es 8. Toma el argumento de tamaño de tabulacion
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Devuelve el indice de la primera aparicion de una subcadena, si no se encuentra devuelve -1
challenge = "thirty days of python"
print(challenge.find("y"))
print(challenge.find("th"))

# rfind(): Devuelve el indice de la ultima aparicion de una subcadena, si no se encuentra devuelve -1
challenge = "thirty days of python"
print(challenge.rfind("y"))
print(challenge.rfind("th"))

# format(): formatea la cadena en una salida mas agradable
first_name = "Gustavo"
last_name = "Pumachagua"
age = 23
job = "teacher"
country = "Peru"
sentence = "I am {} {}. I am {} years old. I live in {}.".format(first_name, last_name, age, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = "The area of a circle with radius {} is {}".format(str(radius), str(area))
print(result)

# index(): devuelve el indice mas bajo de una subcadena, los argumentos adicionales indican el indice inicial y final (predeterminado 0 y longitud de cadena -1). Si no se encuentra la subcadena, genera un valueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))
print(challenge.index(sub_string, 9))

# rindex(): Devuelve el indice mas alto de una subcadena, los argumentos adicionales indican el indice inicial y final (predeterminado 0 y longitud de la cadena -1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string, 9))

# isalnum(): comprueba el caracter alfanumerico
challenge = "ThirtyDaysPython"
print(challenge.isalnum())

challenge = "30DaysPython"
print(challenge.isalnum())

challenge = "thirty days of python"
print(challenge.isalnum())

challenge = "thirty days of python 2019"
print(challenge.isalnum())

# isalpha(): comprueba si todos los elementos de cadena son caracteres alfabeticos (az y AZ).
challenge = "thirty days of python"
print(challenge.isalpha())
challenge = "ThirtyDaysPython"
print(challenge.isalpha())
num = "123"
print(num.isalpha())

# isdecimal(): comprueba si todos los caracteres de una cadena son decimales (0-9).
challenge = "thirty days of python"
print(challenge.isdecimal())
challenge = "123"
print(challenge.isdecimal())
challenge = "\u00B2"
print(challenge.isdigit())
challenge = "12 3"
print(challenge.isdecimal())

# isdigit(): comprueba si todos los caracteres de una cadena son numeros (0-9 y algunos otros caracteres Unicode para numeros)
challenge = "Thirty"
print(challenge.isdigit())
challenge = "30"
print(challenge.isdigit())
challenge = "\u00B2"
print(challenge.isdigit())

# isnumeric(): comprueba si todos los caracteres de una cadena son numeros o estan relacionados con numeros (al igual que isdigit(), solo acepta mas simbolos, como ½).
num = "10"
print(num.isnumeric())
num = "\u00BD"
print(num.isnumeric())
num = "10.5"
print(num.isnumeric())

# isidentifier(): busca un identificador valido; verifica si una cadena es un nombre de variable valido.
challenge = "30DaysOfPython"
print(challenge.isidentifier())
challenge = "thirty_days_of_python"
print(challenge.isidentifier())

# islower(): comprueba si todos los caracteres del alfabeto en la cadena estan en minusculas.
challenge = "thirty days of python"
print(challenge.islower())
challenge = "Thirty days of python"
print(challenge.islower())

# isupper(): comprueba si todos los caracteres del alfabeto en la cadena estan en mayusculas.
challenge = "thirty days of python"
print(challenge.isupper())
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())

# join(): Devuelve una cadena concatenada
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " ".join(web_tech)
print(result)

web_tech = ["HTML", "CSS", "javaScript", "React"]
result = "# ".join(web_tech)
print(result)

# strip(): elimina todos los caracteres dados desde el principio y el final de la cadena.
challenge = "thirty days of pythonnn"
print(challenge.strip("noth"))

# replace(): reemplaza la subcadena con una cadena dada.
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))

# split(): divide la cadena, utilizando la cadena dada o el espacio como separador.
challenge = "thirty days of python"
print(challenge.split())
challenge = "thirty, days, of, python"
print(challenge.split(", "))

# title(): devuelve una cadena de titulo en mayusculas
challenge = "thirty days of python"
print(challenge.title())

# swapcase(): convierte todos los caracteres en mayusculas a minusculas y todos los caracteres en minusculas a caracteres en mayusculas.
challenge = "thirty days of python"
print(challenge.swapcase())
challenge = "Thirty Days Of Python"
print(challenge.swapcase())

# startswith(): comprueba si la cadena comienza con la cadena especificada.
challenge = "thirty days of python"
print(challenge.startswith("thirty"))

challenge = "30 days of python"
print(challenge.startswith("thirty"))

