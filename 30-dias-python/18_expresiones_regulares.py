# Expresiones regulares
"""
Una expresion regular o RegEx es una cadena de texto especial que ayuda a encontrar patrones en los datos.
Se puede usar un RegEx para verificar si esxiste algun patron en un tipo de datos diferente.
Para usar RegEx en Python primero debemos importar el modulo RegEx que llama re.
"""
# El modulo re
"""
Despues de importar el modulo, podemos usarlo detectar o encontrar patrones.
"""
import re

# Modulo Metodos en re
"""
Para encontrar un patron, usamos un conjunto diferente de conjuntos de caracteres re que permiten buscar una coincidencia en una cadena.
* re.match(): busca solo al comienzo de la primera linea de la cadena y devuelve los objetos coincidentes si los encuentra; de lo contrario, devuelve Ninguno.
* re.search: Devuelve un objeto de coincidencia si hay uno en cualquier parte de la cadena, incluidas las cadenas de varias lineas.
* re.findall: Devuelve una lista que contiene todas las coincidencias
* re.split: toma una cadena, la divide en los puntos de coincidencia, devuelve una lista
* re.sub: reemplaza una o varias coincidencias dentro de una cadena
"""
# juego
"""
# syntax
re.match(substring, string, re.I)
"""
import re
txt = "I love to teach python and javaScript"
# It returns an object with span, and match
match = re.match("I love to teach", txt, re.I)
print(match)
# we can get the starting and ending position of the math as tuple using span
span = match.span()
print(span)
# Lets find the start and stop position from the span
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

"""
Como puedo ver en el ejemplo anterior, el patron que estamos buscando (o la subcadena que estamos buscando) es Me encanta enseñar. La funcion de coincidencia devuelve un objeto solo si el texto comienza con el patron.
"""
import re
txt = "I love to teach python and javaScript"
match = re.match("I like to teach", txt, re.I)
print(match)
"""
La cadena no coincide con Me gusta enseñar, por lo tanto, no hubo ninguna coincidencia y el metodo de coincidencia devolvio Ninguno.
"""
# search
"""
# syntax
re.match(substring, string, re.I)
"""
import re
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language
"""
# It returns an object with span and match
match = re.search("first", txt, re.I)
print(match)
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)
# Lets find the start and stop position from the span
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

"""
Como puede ver, la busqueda es mucho mejor que la coincidencia porque puede buscar el patron en todo el texto.
La busqueda devuelve un objeto de coincidencia con una primera coincidencia que se encontro; de lo contario, devuelve None. Una funcion mucho mejor es findall.
Esta funcion busca el patron en toda la cadena y devuelve todas las coincidencias en forma de lista.
"""
# Busqueda de todas las coincidencias mediante findall
# findall() devuelve todas las coincidencias como una lista
import re
txt = """Python is the most beautifull language that a human being has ever created.
I recommend python for a first programming language
"""
# It return a list
matches = re.findall("language", txt, re.I)
print(matches)

"""
Como puede ver, la palabra idioma se encontro dos veces en la cadena.
"""
txt = """Python is the most beautifull language thet a human being has ever created.
I recommend python for a first programming language
"""
# It returns list
matches = re.findall("python", txt, re.I)
print(matches)

"""
Dado que estamos usando re.I, se incluyen letras minusculas. SI no tenemos la bandera re.I, entonces tendremos que escribir nuestro patron de manera diferente
"""
import re
txt = """python is the most beautifull language that a human being has ever created.
I recommend python for a first programming language
"""
matches = re.findall("python|python", txt)
print(matches)
matches = re.findall("[Pp]ython", txt)
print(matches)

# Reemplazo de una subcadena
import re
txt = """python is the most beautifull language that a human being has ever created.
I recommend python for a first programming language
"""
match_replaced = re.sub("Python|python", "javaScript", txt, re.I)
print(match_replaced)
match_replaced = re.sub("[Pp]ython", "javaScript", txt, re.I)
print(match_replaced)

"""
Añadamos un ejemplo mas. La siguiente cadena es muy dificil de leer a menos que eliminemos el simbolo %. Reemplazar el % con una cadena vacia limpiara el texto.
"""
import re
txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?
"""
matches = re.sub("%", "", txt)
print(matches)

# Dividir texto usando RegEx Split
import re
txt = """I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?
"""
print(re.split("\n", txt))

# Escribir patrones RegEx
"""
Para declarar una variable de cadena usamos comillas simpre o dobles.
Para declarar la variable RegEx r.
El siguiente patron solo identifica manzana con minusculas, para que no distinga entre mayusculas y minusculas, debemos reescribir nuestro patron o agregar una bandera.
"""
import re
regex_pattern = r"apple"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)

# To make case insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I)
print(matches)
# or we can use a set of characters method
regex_pattern = r"[Aa]pple"
matches = re.findall(regex_pattern, txt)
print(matches)

"""
[]: un conjunto de caracteres
[ac] significa, a o b o c
[az] significa, cualquier letra de la a a la z
[AZ] significa, cualquier caracter de la A a la Z
[0-3] significa, 0 o 1 o 2 o 3
[0-9] significa cualquier número del 0 al 9
[A-Za-z0-9] cualquier carácter individual, es decir, de la a a la z, de la A a la Z o del 0 al 9
\: utiliza para escapar caracteres especiales
\d significa: coincidencia donde la cadena contiene dígitos (números del 0 al 9)
\D significa: coincidencia donde la cadena no contiene dígitos
. : cualquier carácter excepto el carácter de nueva línea (\n)
^: comienza con
r'^subcadena', por ejemplo, r'^amor', una oración que comienza con una palabra amor
r'[^abc] significa no a, no b, no c.
$: termina en
r'substring$', por ejemplo, r'love$', oración que termina con una palabra love
*: cero o más veces
r'[a]*' significa un opcional o puede ocurrir muchas veces.
+: una o más veces
r'[a]+' significa al menos una vez (o más)
?: cero o una vez
real academia de bellas artes]?' significa cero veces o una vez
{3}: exactamente 3 caracteres
{3,}: al menos 3 caracteres
{3,8}: de 3 a 8 caracteres
|: Cualquiera o
r'apple|banana' significa manzana o plátano
(): Captura y grupo
"""
# corchete
"""
Usemos corchetes para incluir mayusculas y minusculas
"""
import re
regex_pattern = r"[Aa]pple"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)

# Si queremos buscar el platano, escribimos el patron de la siguiente manera:
import re
regex_pattern = r"[Aa]pple|[Bb]anana"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)
"""
Usando el corchete y el operador or, logramos extraer Apple, apple, Banana y banana.
"""
# Caracter de escape (\) en RegEx
import re
regex_pattern = r"\d"
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)

# una o mas veces (+)
import re
regex_pattern = r"\d+"
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)

# Periodo(.)
import re
regex_pattern = r"[a]."
txt = """ Apple and banana are fruits
"""
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"[a].+"
matches = re.findall(regex_pattern, txt)
print(matches)

# cero o mas veces (*)
"""
Cero o muchas veces. El patron puede no ocurrir o puede ocurrir muchas veces.
"""
import re
regex_pattern = r"[a].*"
txt = """Apple and banana are fruits"""
matches = re.findall(regex_pattern, txt)
print(matches)

# cero o una vez (?)
"""
Cero o una vez. El patron no ocurrir o puede ocurrir una vez.
"""
import re
txt = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""
regex_pattern = r"[Ee]-?mail"
matches = re.findall(regex_pattern, txt)
print(matches)

# Cuantificador en RegEx
"""
Podemos especificar la longitud de la subcadena que estamos buscando en un texto, usando una llave. Imaginemos, nos interesa una subcadena con una longitud de 4 caracteres:
"""
import re
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"\d{4}"
matches = re.findall(regex_pattern, txt)
print(matches)

txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"\d{1, 4}"
matches = re.findall(regex_pattern, txt)
print(matches)

# Carrito ^
# Starts with
import re
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"^This"
matches = re.findall(regex_pattern, txt)
print(matches)

# Negacion
import re
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"[^A-Za-z ]+"
matches = re.findall(regex_pattern, txt)
print(matches)