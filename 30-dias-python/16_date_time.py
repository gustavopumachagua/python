# Python Date time
# Fecha y hora de python
"""
Python tiene un modulo de fecha y hora para manejar la fecha y la hora.
"""
import datetime
print(dir(datetime))
["MAXYEAR", "MINYEAR", "__builtins__", "__cached__", "__doc__", "__file__", "__loader__", "__name__", "__package__", "__spec__", "date", "datetime", "datetime_CAPI", "sys", "time", "timedelta", "timezone", "tzinfo"]

"""
Con los comandos integrados dir o help es posible conocer las funciones disponibles en un determinado modulo.
Como puedes ver, em el modulo datetime hay muchas funciones, pero nos centraremos en date, datetime, time y timedelta. Vamos a verlos uno por uno.
"""
# Obtener informacion de fecha y hora
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

"""
La marca de tiempo o la marca de tiempo de Unix es la cantidad de segundos transcurridos desde el 1 de enero de 1970 UTC.
"""
# Formato de salida de fecha usando strftime
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f"{day}/{month}/{year}, {hour}:{minute}")


from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time: ", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one: ", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/yy H.M:S format
print("time two: ", time_two)

"""
Aqui estan todos los simbolos strftime que usamos para formatear el tiempo.
"""
# Cadena a tiempo usando strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string = ", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object = ", date_object)

# Usando la fecha de fecha y hora
from datetime import date
d = date(2020, 1, 1)
print(d)
print("Current date: ", d.today())
# date object of today's date
today = date.today()
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)

# Objetos de tiempo para representar el tiempo
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b = ", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c = ", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d = ", d)

# Diferencia entre dos puntos en el tiempo usando
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year: 27 days, 0:00:00
print("Time left for new year: ", time_left_for_newyear)

t1 = datetime(year =2019, month = 12, day =5, hour =0, minute = 59, second =0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print("Time left for new year: ", diff)

# Diferencia entre dos puntos en el tiempo utilizando timedelta
from datetime import timedelta
t1 = timedelta(weeks = 12, days = 10, hours = 4, seconds = 20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)