# Clases y Objetos
"""
Python es un lenguaje de programacion orientado a objetos. Todo en Python es un objeto, con sus propiedades y metodos. Un numero, cadena, lista, diccionario, tupla, conjunto, etc.
Utilizado en un programa es un objeto de una clase integrada correspondiente. Creamos clase para crear un objeto. Una clase es como un constructor de objetos o un "modelo" para crear objetos.
Instanciamos una clase para crear un objeto. La clase define los atributos y el comportamiento del objeto, mientras que el objeto, por otro lado, representa la clase.
Hemos estado trabando con clases y objetos desde el comienzo de este desafio sin saberlo. Cada elemento en un programa de Python es un objeto de una clase.Comprobemos si todo en Python es una clase:
"""
"""
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
"""
# Crear una clase
"""
Para crear una clase necesitamos la palabra clave clase seguida del nombre y dos puntos. El nombre de la clase debe ser CamelCase.

# syntax
class ClassName:
  code goes here
"""
# Ejemplo:
class Person:
  pass
print(Person)

#Crear un objeto
"""
Podemos crear un objeto llamando a la clase.
"""
p = Person()
print(p)

# Constructor de clase
"""
En los ejemplos anteriores, hemos creado un objeto de la clase Person. Sin embargo, una clase sin constructor no es realmente util en aplicaciones reales.
Usemos la funcion constructora para que nuestra clase sea mas util. Al igual que la funcion constructora en java o javaScript, Python tambien tiene una funcion constructora init () incorporada. La funcion constructora init tiene un parametro propio que es una referencia a la instancia actual de la clase
Ejemplo:
"""
class Person:
  def __init__(self, name):
    self.name=name
p = Person("Gustavo")
print(p.name)
print(p)

# Agreguemos mas parametros a la funcion constructora.
class Person:
  def __init__(self, firstname, lastname, age, country, city):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
p = Person("Gustavo", "Pumachagua", 20, "Peru", "Lima")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Metodos de objetos
"""
Los objetos pueden tener metodos. Los metodos son funciones que pertenecen al objeto.
"""
# Ejemplo:
class Person:
  def __init__(self, firstname, lastname, age, country, city):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
def person_info(self):
  return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}'
p = Person("Gustavo", "Pumachagua", 25, "Peru", "Lima")
print(p.person_info())

# Metodos predeterminados de objetos
"""
A veces, es posible que tener valores predeterminados para sus metodos de objeto. Si damos valores predeterminados para los parametros en el constructor, podemos evitar errores cuando llamamos o instanciamos nuestra clase sin parametros.
"""
# Ejemplo:
class Person:
  def __init__(self, firstname = "Gustavo", lastname = "Pumachagua", age = 20, country = "Peru", city = "Lima"):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
  def person_info(self):
    return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
p1 = Person()
print(p1.person_info())
p2 = Person("Gustavo", "Pumachgua", 30, "Nomanland", "Noman city")
print(p2.person_info())

# Metodo para modificar los valores predeterminados de la clase
"""
En el siguiente ejemplo, la clase de persona, todos los parametros del constructor tiene valores predeterminados. Ademas de eso, tenemos el parametro de habilidades, al que podemos acceder usando un metodo. Vamos a crear el metodo add_skill para agregar habilidades a la lista de habilidades.
"""
class Person:
  def __init__(self, firstname = "Gustavo", lastname = "Pumachagua", age = 18, country = "Peru", city = "Lima"):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
    self.skills = []
  def perso_info(self):
    return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
  def add_skill(self, skill):
    self.skills.append(skill)
p1 = Person()
print(p1.perso_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person("Gustavo", "Doe", 30, "Nomanland", "Noman city")
print(p2.perso_info())
print(p1.skills)
print(p2.skills)

# Herencia
"""
Usando la herencia podemos reutilizar el codigo de la clase principal. La herencia nos permite definir una clase que hereda todos los metodos y propiedades de la clase padre.
La clase o superclase o clase base es la clase que proporciona todos los metodos y propiedades. La clase secundaria es la clase que hereda de otra clase principal
"""
class Student(Person):
  pass
s1 = Student("Eyob", "Perez", 30, "Peru", "Lima")
s2 = Student("Gustavo", "Pumachagua", 28, "Peru", "Lima")
print(s1.perso_info())
s1.add_skill("javaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)
print(s2.perso_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Markenting")
print(s2.skills)
"""
No llamamos al constructor init () en la clase secundaria. Si no lo llamamos, aun podemos acceder a todas las propiedades desde el padre. Pero si llamamos al constructor, podemos acceder a las propiedades principales llamando a super.
Podemos agregar un nuevo metodo al elemento secundario o podemos anular los metodos de la clase principal creando el mismo nombre de metodo en la clase secundaria. Cuando agregamos la funcion init(), la clase secundaria ya no heredara la funcion init () de los padres.
"""
# Anulacion del metodo principal
class Student(Person):
  def __init__(self, firstname="Gustavo", lastname="Pumachagua", age=18, country="Peru", city="Lima", gender = "male"):
    self.gender = gender
    super().__init__(firstname, lastname, age, country, city)
  def perso_info(self):
    gender = "He" if self.gender == "male" else "she"
    return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'
s1 = Student("Eyob", "Yetayeh", 30, "Peru", "Lima", "male")
s2 = Student("Lidiya", "Perez", 28, "Peru", "Lima", "female")
print(s1.perso_info())
s1.add_skill("javaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)
print(s2.perso_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)
"""
Podemos usar la función integrada super() o el nombre del padre Persona para heredar automáticamente los métodos y propiedades de su padre. En el ejemplo anterior, anulamos el método principal. El método del niño tiene una característica diferente, puede identificar si el género es masculino o femenino y asignar el pronombre adecuado (Él/Ella).
"""