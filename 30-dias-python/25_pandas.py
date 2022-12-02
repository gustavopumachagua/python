# Pandas
"""
Pandas es una estructura de datos y herramientas de analisis de datos de codigo abierto, alto rendimiento y facil de usar para el lenguaje de programacion python. Pandas agrega estructuras de datos y herramientas diseñadas para trabajar con datos similares a tablas, que son series y data frames. Pandas porporciona herramientas para la manipulacion de datos:
* reorganizacion
* fusionando
* clasificacion
* rebanar
* agregacion
* imputacion si esta utilizando anaconda, no tiene que instalar pandas.
"""
# Instalando pandas
# Para Mac
"""
pip install conda
conda install pandas
"""
# Para windows
"""
pip install conda
pip install pandas
"""
"""
La estructura de datos de pandas se basa en Series y DataFrames.
Una serie es una columna y un DataFrame es una tabla multidimensional compuesta por una coleccion de series. Para crear una serie de pandas, debemos usar numpy para crear matrices unidimensionales o una lista de python
"""
# Importacion de pandas
import pandas as pd
import numpy as np
# Creacion de series pandas con indice predeterminado
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

# Creacion de series Pandas con indice personalizado
import pandas as pd
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index = [1, 2, 3, 4, 5])
print(s)

fruits = ["Orange", "Banana", "Mango"]
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creacion de series Pandas a partir de un diccionario
import pandas as pd
dct = {"name":"Gustavo", "country":"Peru", "city":"Lima"}
s= pd.Series(dct)
print(s)

# Crear una serie de pandas constantes
import pandas as pd
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creando una serie pandas usando linspace
import pandas as pd
import numpy as np
s = pd.Series(np.linspace(5, 20, 10))
print(s)

# marcos de datos
"""
Los marcos de datos de Pandas se pueden crear de diferentes maneras.
"""
# Creacion de tramas de datos a partir de una lista de listas
import pandas as pd
data = [
  ["Gustavo", "Peru", "Lima"],
  ["Ruben", "UK", "London"],
  ["John", "España", "Madrid"]
]
df = pd.DataFrame(data, columns=["Names", "Country", "City"])
print(df)

# Creacion de DataFrame usando el diccionario
import pandas as pd
data = {"Name": ["Gustavo", "David", "John"], "Country":[
  "Colombia", "UK", "Peru"], "City":["Bogota", "London", "Lima"]}
df = pd.DataFrame(data)
print(df)

# Crear tramas de datos a partir de una lista de diccionarios
import pandas as pd
data = [
  {"Name":"Gustavo", "Country":"Peru", "City":"Lima"},
  {"Name":"David", "Country":"UK", "City":"London"},
  {"Name":"John", "Country":"Colombia", "City":"Bogota"}
]
df = pd.DataFrame(data)
print(df)

# Leer archivo CSV usando Pandas
"""
Para descargar el archivo CSV, lo que se necesita en este ejemplo, consola/linea de comando es suficiente:
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
"""
# coloque el archivo descargado en su directorio de trabajo.
import pandas as pd
df = pd.read_csv('weight-height.csv')
print(df)

# Exploracion de datos
"""
Leamos solo las primeras 5 filas usando head()
"""
print(df.head())

"""
Exploremos tambien las ultimas grabaciones del dataframe usando los metodos tail().
"""
print(df.tail())
"""
Como puede ver, el archivo csv tiene tres filas: Genero, Altura y Peso. Si el DataFrame tuviera filas largas, seria dificil conocer todas las columnas. Por lo tanto, debemos usar un metodo para conocer las columnas. No sabemos el numero de filas. Usemos el metodo de forma.
"""
print(df.shape)
# Obtengamos todas las columnas usando columnas.
print(df.columns)
