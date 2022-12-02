# Python para analisis estadistico
# estadisticas
"""
La estadistica es la disciplina que estudia la recopilacion, organizacion, visualizacion, analisis, interpretacion y presentacion de datos.
La estadistica es una rama de las matematicas que se recomienda como requisito previo para la ciencia de datos y el aprendizaje automatico. La estadisca es un campo muy amplio pero nos centraremos en esta seccion solo en la parte mas relevante.
Despues de completar este desafio y la ciencia de datos. Cualquiera que sea el camino que pueda seguir, en algun momento de su carrera obtendra datos en los que puede trabajar. Tener algunos conocimientos estadisticos te ayudara a tomar decisiones basadas en datos, los datos dicen como dicen.
"""
# Datos
"""
¿Que son los datos? Los datos son cualquier conjunto de caracteres que se recopilan y traducen para algun proposito, generalmente analisis. Puede ser cualquier caracter, incluidos texto y numeros, imagenes, sonido o video.
Si los datos no se ponen en un contexto, no tienen ningun sentido para un ser humano o una computadora. Para dar sentido a los datos, necesitamos trabajar en los datos utilizando diferentes herramientas.

El flujo de trabajo del analisis de datos, la ciencia de datos o el aprendizaje automatico parte de los datos. Los datos se pueden proporcionar desde alguna fuente de datos o se pueden crear. Hay datos estructurados y no estructurados.
Los datos se pueden encontrar en formato pequeño o grande. La mayoria de los tipos de datos que obtendremos se han cubierto en la seccion de manejo de archivos.
"""
# Modulo de estadisticas
"""
El modulo de estadisticas de Python proporciona funciones para calcular estadisticas matematicas de datos numericos. El modulo no pretende ser un competidor de bibliotecas de terceros, como NumPy, SciPy, o paquetes de estadisticas propietarios completos destinados a estadisticos profesionales, como Minitab, SAS y Matlab. Esta dirigido al nivel de gratificadores y calculadoras cientificas.
"""
# NumPy
"""
En la primera seccion, definimos a Python como un gran lenguaje de programcion de proposito general por si solo, pero con la ayuda de otras bibliotecas populares como (numpy, scipy, matplotlib, pandas, etc.) se convierte en un poderoso entorno para la computacion cientifica.
Numpy es la biblioteca central para computacion cientifica en Python.
Proporciona un objeto de matriz multidimensional de alto rendimiento y herramientas para trabajar con matrices.
Hasta ahora, hemos estado vscode, pero a partir de ahora recomendaria usar jupyter Notebook. Para acceder a jupyter notebook, instalemos anaconda.
Si esta utilizando anaconda, la mayoria de los paquetes comunes estan incluidos y no tiene paquetes de instalacion si instalo anaconda.
"""
"""
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
"""
# Importando Numpy
"""
jupyter notebook esta disponible si esta a favor jupyter notebook
"""
# How to import numpy
import numpy as np
# How to check the version of the numpy package
print("numpy: ", np.__version__)
# Checking the available methods
print(dir(np))

#  Creando una matriz numpy usando
# Creacion de matrices int numpy
# Creating python list
python_list = [1, 2, 3, 4, 5]
# Checking data types
print("Type: ", type(python_list))
print(python_list)
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)
# Creating Numpy
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creacion de matrices numpy numpy flotantes
"""
Creacion de una matriz numpy flotantes de la lista con un parametro de tipo de datos flotante
"""
# Python list
import numpy as np
python_list = [1, 2, 3, 4, 5]
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

# Creacion de matrices numpy booleanas
"""
Crear una matriz booleana a numpy de lista
"""
import numpy as np
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# Creando una matriz multidimensional usando numpy
"""
Una matriz puede tener una o varias filas y columnas
"""
import numpy as np
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Convertir matriz numpy a lista
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print("one dimensional array: ", np_to_list)
print("two dimensional array: ", numpy_two_dimensional_list.tolist())

# Creando una matriz numpy a partir de una tupla
# Numpy array from tuple
# Creating tuple in python
import numpy as np
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print("python_tuple: ", python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print("numpy_array_from_tuple: ", numpy_array_from_tuple)

# Forma de matriz numpy
"""
El metodo de forma proporciona la forma de la matriz como una tupla. La primera es la fila y la segunda es la columna. Si la matriz es solo unidimensional, devuelve el tamaño de la matriz.
"""
import numpy as np
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
[4,5,6,7],
[8,9,10, 11]])
print(three_by_four_array.shape)

# Tipo de datos de matriz numpy
"""
Tipo de tipos de datos: str, int, float, complex, bool, list, None
"""
import numpy as np
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Tamaño de una matriz numpy
"""
En numpy para saber la cantidad de elementos en una lista de matriz numpy usamos el tamaño
"""
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("The size; ", numpy_array_from_list.size)
print("The size: ", two_dimensional_list.size)

# Operacion matematica usando numpy
"""
La matriz NumPy no es exactamente como la lista de python. Para realizar una operacion matematica en la lista de Python, tenemos que recorrer los elementos, pero numpy puede permitir realizar cualquier operacion matematica sin realizar un bucle. Operacion matematica:
* suma (+)
* Resta (-)
* Multiplicacion (*)
* Division (/)
* Modulos (%)
* Division de piso (//)
* Exponencial (**)
"""
# Suma
# Mathematical Operation
# Addition
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

# Sustraccion
# subtraction
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

# Multiplicacion
# Multiplication
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

# Division
# Division
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

# Modulo
# Modulus; Finding the remainder
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# Division de piso
# Floor division: the division result without the remainder
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# Exponencial
# Exponencial is finding some number the power of another:
import numpy as np
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)

# Comprobacion de tipos de datos
# Int, Float numbers
import numpy as np
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype="bool")
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Tipos de conversion
"""
Podemos convertir los tipos de datos de la matriz numpy
"""
# 1. Int a Flotante
import numpy as np
numpy_int_arr = np.array([1, 2, 3, 4], dtype="float")
numpy_int_arr
print(numpy_int_arr)

# 2. Floatante a int
import numpy as np
numpy_int_arr = np.array([1., 2., 3., 4.], dtype="int")
numpy_int_arr
print(numpy_int_arr)

# 3. int a booleano
import numpy as np
print(np.array([-3, -2, 0, 1, 2, 3], dtype="bool"))

# 4. Int a Str
import numpy as np
numpy_float_list.astype('int').astype('str')

# Matrices multidimensionales
# 2 Dimension Array
import numpy as np
two_dimensional_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimensional_array))
print("Shape: ", two_dimensional_array.shape)
print("Size: ", two_dimensional_array.size)
print("Data type: ", two_dimensional_array.dtype)

# Obtener elementos de una matriz numpy
# 2 Dimension Array
import numpy as np
two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimensional_array[0]
second_row = two_dimensional_array[1]
third_row = two_dimensional_array[2]
print("First row: ", first_row)
print("Second row: ", second_row)
print("Third row: ", third_row)

first_column = two_dimensional_array[:,0]
second_column = two_dimensional_array[:,1]
third_column = two_dimensional_array[:,2]
print("First column: ", first_column)
print("Second column: ", second_column)
print("Third column: ", third_column)
print(two_dimensional_array)

# Rebanar matriz Numpy
"""
Cortar en numpy es similar a cortar en la lista de Python
"""
import numpy as np
two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_colums = two_dimensional_array[0:2, 0:2]
print(first_two_rows_and_colums)

# ¿Como invertir las filas y toda la matriz?
"""two_dimensional_array[::]
array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""

# Invertir las posiciones de fila y columna
import numpy as np
two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimensional_array[::-1, ::-1])

# ¿Como representar los valores perdidos?
print(two_dimensional_array)
two_dimensional_array[1,1] = 55
two_dimensional_array[1,2] = 44
print(two_dimensional_array)
# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order="c")
numpy_zeroes = np.zeros((3, 3), dtype=int, order="C")
numpy_zeroes
#Numpy Zeroes
numpy_ones = np.ones((3,3), dtype=int, order="C")
print(numpy_ones)
twoes = numpy_ones * 2

# Reshape
# numpy.reshape(), numpy.flatten()
import numpy as np
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)

# Horitzontal Stack
import numpy as np
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print(np_list_one + np_list_two)
print("Horizontal Append: ", np.hstack((np_list_one, np_list_two)))
# Vertical Append
print("Vertical Append: ", np.vstack((np_list_one, np_list_two)))

# Generacion de numeros aleatorios
# Generate a random float number
import numpy as np
random_float = np.random.random()
print(random_float)

# Generate a random float number
import numpy as np
random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10
import numpy as np
random_int = np.random.randint(0, 11)
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array
import numpy as np
random_int = np.random.randint(2, 10, size = 4)
print(random_int)

# Generating a random integers between 0 and 10
import numpy as np
random_int = np.random.randint(2, 10, size=(3, 3))
print(random_int)

# Generacion de numeros aleatorios
# np.random.normal(mu, sigma, size)
import numpy as np
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

# Numpy y estadisticas
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)

# Matriz en numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
four_by_four_matrix
"""
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])
"""
np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix
"""
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])
"""
# Numpy numpy.arange()
"""
¿Que es Organizar?
A veces, desea crear valores que esten espaciados uniformemente dentro de un intervalo definido. Por ejemplo, desea crear valores del 1 al 10; puedes usar la funcion numpy.arange()
"""
# Creating list using range(starting, stop, step)
lst = range(0, 11, 2)
lst
range(0, 11, 2)
for l in lst:
  print(l)

# Similar to range arange numpy.arange(start, stop, step)
import numpy as np
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)

# Crear secuencia de numeros usando linspace
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)

# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)

x.itemsize

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
np_list

print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

# Funciones estadisticas NumPy con ejemplo
"""
NumPy tiene funciones estadisticas bastante utiles para encontrar el minimo, el maximo, la media, la mediana, el percentil, la desviacion y la varianza, etc. de los elementos dados en la matriz. Las funciones se explican a continuacion: la funcion estadistica Numpy esta equipada con la funcion estadistica robusta que enumera a continuacion
"""
"""
Funciones numericas
* Min np.min()
* Max np.max()
* Media np.media()
* Varianza
* Percentil
* Desviacion estandar np.std()
"""
import numpy as np
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print("min: ", two_dimensional_array.min())
print("max: ", two_dimensional_array.max())
print("mean: ", two_dimensional_array.mean())
# print("median: ", two_dimension_array.median())
print("sd: ", two_dimensional_array.std())

