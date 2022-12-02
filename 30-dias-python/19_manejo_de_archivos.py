# Manejo de archivos
"""
Hasta ahora hemos visto diferentes tipos de datos de Python. Por lo general, almacenamos nuestros datos en diferentes formatos de archivo. Ademas del manejo de archivos, tambien veremos diferentes formatos de archivo (.txt, .json, .xml, .csv, .tsv, .excel) en esta seccion.   primero, familiaricemonos con el manejo de archivos con formato de archivo comun (.txt).
El manejo de archivos es una parte importante de la programacion que nos permite crear, leer, actualizar y eliminar archivos. En Python, para manejar datos, usamos la funcion integrada open().

# Syntax
open("filename", mode)
"""
"""
"r" - Lectura - Valor predeterminado. Abre un archivo para lectura, devuelve un error si el archivo no existe
"a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
"w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
"x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
"t" - Texto - Valor por defecto. Modo de texto
"b" - Binario - Modo binario (por ejemplo, imágenes)
"""
# Abrir archivos para leer
"""
El modo predeterminado de apertura es lectura, por lo que no tenemos que especificar "r" o "rt". Cree y guarde un archivo llamado read_file_example.txt en el directorio de archivos
"""
f = open("./read_file_example.txt","w")
print(f)
"""
Como puede ver en el ejemplo anterior, imprime el archivo abierto y brindo informacion al respecto. El archivo abierto tiene diferentes metodos de lectura:
red(), readline, readlines. Un archivo abierto debe cerrarse con el metodo. close().
* read(): lee todo el texto como una cadena. Si queremos limitar el numero de caracteres que queremos leer, podemos limitarlo pasando el valor int al metodo read(number).
"""
f = open("./read_file_example.txt")
txt = f.read()
print(type(txt))
print(txt)
f.close()
"""
En lugar de imprimir todo el texto, imprimamos los primeros 10 caracteres del archivo de texto.
"""
f = open("./read_file_example.txt")
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
"""
readline(): lee todo el texto linea y devuelve una lista de lineas
"""
f = open("./read_file_example.txt")
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
"""
Otra forma de obtener todas las lineas como una lista es usando splitlines():
"""
f = open("./read_file_example.txt")
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

"""
Despues de abrir un archivo, debemos cerrarlo. Hay una alta tendencia a olvidarse de cerrearlos. Hay una nueva forma de abrir archivos usando with - cierra los archivos por si mismo. Reescribamos el ejemplo anterior con el metodo with:
"""
with open("./read_file_example.txt") as f:
  lines = f.read().splitlines()
  print(type(lines))
  print(lines)

# Abrir archivos para escribir y actualizar
"""
Para escribir en un archivo existente, debemos agregar un modo como parametro a la funcion open():
* "a"-agregar- se agregara al final del archivo, si el archivo no lo hace, crea un nuevo archivo.
* "w" -escribir- sobrescribira cualquier contenido existente, si el archivo no existe, lo crea.
agreguemos algo de texto al rchivo que hemos estado leyendo:
"""
with open("./read_file_example.txt", "a") as f:
  f.write("This text has to be appended at the end")
"""
El siguiente metodo crea un nuevo archivo, si el archivo no existe:
"""
with open("./read_file_example.txt", "w") as f:
  f.write("This text will be written in a newly created file")

# Eliminacion de archivos
"""
Hemos visto en la seccion anterior como crear y eliminar un dirextorio usando el modulo os. Nuevamente ahora, si queremos eliminar un archivo, usamos el modulo os.
"""
import os
os.remove("./read_file_example.txt")

"""
Si el archivo no existe, el metodo de eliminacion generara un error, por lo que es bueno usar una condicion como esta:
"""
import os
if os.path.exists("./read_file_example.txt"):
  os.remove("./read_file_example.txt")
else:
  print("The file does no exist")

# Tipos de archivo
#Archivo con extension txt
"""
El archivo con extension txt es una forma de datos muy comun y lo hemos cubierto en la seccion anterior. Pasemos al archivo JSON.
"""
# Archivo con extension JSON
"""
JSON significa Notacion de objetos de javaScript. En realidad, es un objeto de javaScript en forma de cadena o un diccionario de Python.
Ejemplo:
"""
# dictionary
person_dct = {
  "name":"Gustavo",
  "country":"Peru",
  "city":"Lima",
  "skills":["javaScript", "React", "Python"]
}
# JON: A string form a dictionary
person__json = "{'name':'Gustavo', 'country':'Peru', 'city':'Lima', 'skills':['javaScript', 'React', 'Python']}"
# we use three quotes and make it multiple line to make it more readable
person__json = """{
  "name":"Gustavo",
  "country":"Peru",
  "city":"Lima",
  "skills":["javaScript", "React", "Python"]
  }"""

# Cambiar JSON A Diccionario
"""
Para cambiar un JSON a un diccionario, primero importamos el modulo json y luego usamos el metodo de carga.
"""
import json
# JSON
person_json = """{
  "name":"Gustavo",
  "country":"Peru",
  "city":"Lima",
  "skills":["javaScript", "React", "Python"]
  }"""
#let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct["name"])

# Cambio de diccionario a JSON
"""
Para cambiar un diccionario a JSON, usamos el metodo dumps del modulo json.
"""
import json
# python dictionary
person = {
  "name":"Gustavo",
  "country":"Peru",
  "city":"Lima",
  "skills":["javaScript", "React", "Python"]
}
# let's convert it to json
person_json = json.dumps(person, indent = 4)
print(type(person_json))
print(person_json)

# Guardar como archivo JSON
"""
Tambien podemos guardar nuestros datos un archivo json. Guardemoslo como un archivo json siguiendo los siguientes pasos. Para escribir un archivo json, usamos el metodo json.dump(), puede tomar diccionario, archivo de salida, sure_ascii y sangria.
"""
import json
# python dictionary
person = {
  "name":"Gustavo",
  "country":"Peru",
  "city":"Lima",
  "skills":["javaScript", "React", "Python"]
}
with open("./json_example.json", "w", encoding="utf-8") as f:
  json.dump(person, f, ensure_ascii=False, indent=4)

"""
En el codigo anterior, usamos codificacion y sangria. La sangria hace que el archivo json sea facil de leer.
"""
# Archivo con extension csv
"""
CSV significa valores separados por comas. CSV es un formato de archivo simple que se utiliza para almacenar datos tabulares, como una hoja de acalculo o una base de datos. CSV es un formato de datos muy comun en la ciencia de datos.

Ejemplo:
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
"""
# Ejemplo:
import csv
with open("./csv_example.csv") as f:
  csv_reader = csv.reader(f, delimiter=",")
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f'columns names are :{", ".join(row)}')
      line_count += 1
    else:
      print(
        f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
      line_count += 1
  print(f'Number of lines: {line_count}')

# Archivo con extension xlsx
"""
Para leer archivo de excel necesitamos instalar el paquete xlrd. Cubriremos esto despues de que cubramos la instalacion del paquete usando pip.
"""
import xlrd
excel_book =xlrd.open_workbook("sample.xls")
print(excel_book.nsheets)
print(excel_book.sheet_names)

# Archivo con extension xml
"""
XML es otro formato de datos estructurados que se parece a HTML. En XML, las etiquetas no estan predefinidas. la primera linea es una declaracion XML. la etiqueta de persona es la raiz del XML. La persona tiene un atributo de genero.
"""
# EJEMPLO: XML
"""
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
"""
import xml.etree.ElementTree as ET
tree = ET.parse('./xml_example.xml')
root = tree.getroot()
print('Root tag: ', root.tag)
print('Attribute: ', root.attrib)
for child in root:
  print("file: ", child.tag)