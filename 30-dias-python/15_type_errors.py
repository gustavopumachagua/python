# Python Type Errors
"""
Cuando escribimos codigos, es comun que cometamos un error tipografico o algun otro error comun.
Si nuestro codigo no se ejecuta, el interprete de python mostrara un mensaje que contiene comentarios con informacion sobre donde ocurre el problema y el tipo de error. A veces tambien nos da sugerencias sobre una posible solucion.
Comprender los diferentes tipos de errores en los lenguajes de programacion nos ayudara a depurar nuestro codigo rapidamente y tambien nos hara mejores en lo que hacemos.
Veamos los tipos de errores mas comunes uno por uno. Primero, abramos y escriba "python". Se abrira el shell interactivo de python.
"""
# Error de sintaxis
# Ejemplo 1 : error de sintaxis
"""
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
"""

"""
Como puede ver, cometimos un error de sintaxis porque olvidamos encerrar la cadena entre parentesis y python ya sugiere la solucion. Arreglemoslo
"""