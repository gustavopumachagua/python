# web scraping
"""
¿Que es el web scraping?
Internet esta lleno de una gran cantidad de datos que se pueden utilizar para diferentes propositos. Para recopilar estos datos, necesitamos saber como extraer datos de un sitio web.
El web scraping es el proceso de extraer y recopilar datos de sitios web y almacenarlos en una maquina local o en una base de datos.
En esta seccion, usaremos beautifulsoup y Requests Package para extraer datos.
La version del paquete que estamos usando es beautifulsoup 4.
Para comenzar a rastrear sitios web, necesita solicitudes, beautifoulSoup4 y un sitio web.
"""
"""
pip install requests
pip install beautifulsoup4
"""
"""
Para extraer datos de sitios web, se necesita una comprension basica de las etiquetas HTML y los selectores CSS. Nos dirigimos al contenido de un sitio web mediante etiquetas HTML, clases o identificadores. Importemos las solicitudes y el modulo BeautifulSoup
"""
"""
import requests
from bs4 import BeautifulSoup
"""
"""
Declaremos la variable url para el sitio web que vamos a raspar.
"""

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

"""
Usando beautifulSoup para analizar el contenido de la pagina
"""
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)