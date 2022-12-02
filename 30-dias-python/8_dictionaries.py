# dictionaries
"""
Un diccionario es una coleccion de tipos de datos no ordenados, modificables (mutables) emparejados (claves: valor)
"""
# Creacion de un diccionario
"""
Para crear un diccionario usamos corchetes, {} o la funcion integrada dict().
"""
# syntax
empty_dict = {}
# Dictionary with data values
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}

# ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":25,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "React", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street":"Space street",
    "zipcode":"02210"
  }
}

"""
El diccionario anterior muestra que un valor puede ser cualquier tipo de datos:
cadena, booleano, lista, tupla, conjunto o un diccionario.
"""
# Longitud del diccionario
"""
Comprueba el numero de pares "clave: valor" en el diccionario.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
print(len(dct))

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
print(len(person))

# Acceso a elementos del diccionario
"""
Podemos acceder a los elementos del diccionario haciendo referencia a su nombre clave.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
print(dct["key1"])
print(dct["key4"])

# Ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":20,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street": "Space street",
    "zipcode": "02210",
  }
}
print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])
print(person["city"])

"""
Acceder a un elemento por nombre de clave genera un error si la clave no existe. Para evitar este error, primero debemos verificar si existe una clave o podemos usar el metodo get.
El metodo get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.
"""
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":20,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street":"Space street",
    "zipcode":"02210"
  }
}
print(person.get("first_name"))
print(person.get("country"))
print(person.get("skills"))
print(person.get("city"))

# Adicion de elementos a un diccionario
"""
Podemos agregar nuevos pares de clave y valor a un diccionario
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
dct["key5"] = "value5"

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
person["job_title"] = "Instructor"
person["skills"].append("HTML")
print(person)

# Modificacion de elementos en un diccionario
"""
Podemos modificar elementos en un diccionario.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
dct["key1"] = "value-one"

# Ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":25,
  "country":"Perez",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street":"Space street",
    "zipcode":"02210"
  }
}
person["first_name"] = "Ruben"
person["age"] = 18

# Comprobacion de claves en un diccionario
"""
Usamos el operador in para verificar si existe una clave en un diccionario
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
print("key2" in dct)
print("key5" in dct)

# Eliminacion de pares de clave y valor de un diccionario
"""
* pop(clave): elimina el elemento con el nombre de clave especificado

* popitem(): elimina el ultimo elemento

* del: elimina un elemento con el nombre de clave especificado
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
dct.pop("key1")
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
dct.popitem()
del dct["key2"]

# Ejemplo:
person = {
  "first_name":"Gustavo",
  "last_name":"Pumachagua",
  "age":25,
  "country":"Peru",
  "is_marred":True,
  "skills":["javaScript", "ReactJS", "NodeJS", "MongoDB", "Python"],
  "address":{
    "street": "Space street",
    "zipcode": "02210"
  }
}
person.pop("first_name")
person.popitem()
del person["is_marred"]

# Cambio de diccionario a una lista de elementos
"""
El metodo items() cambia el diccionario a una lista de tuplas.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
print(dct.items())

# Borrar un diccionario
"""
Si no queremos los elementos en un diccionario, podemos borrarlos usando el metodo clear().
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
print(dct.clear())

# Eliminacion de un diccionario
"""
Si no usamos el diccionario podemos borrarlo por completo
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
del dct

# Copiar un diccionario
"""
Podemos copiar un diccionario usando un metodo copy().
Usando la copia podemos evitar la mutacion del diccionario original.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
dct_copy = dct.copy()

# Obtener claves de diccionario como una lista
"""
El metodo keys() nos da todas las claves de un diccionario en forma de lista.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
keys = dct.keys()
print(keys)

# Obtener valores de diccionario como una lista
"""
El metodo de valores nos da todos los valores de un diccionario como una lista.
"""
# syntax
dct = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4"}
values = dct.values()
print(values)