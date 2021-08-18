import gzip

######################################################################

"""
Estos ejercicios usan el archivo `Data/camion.csv`.
El archivo contiene una lista de líneas con información sobre
los cajones de fruta cargados en un camión.
Suponemos que estás trabajando en el directorio `ejercicios_python/`
del curso.
"""

"""
2.1
Leer archivo entero en una sola cadena.
"""
def preliminar(nombre_archivo):
  """Abrir y leer datos de un archivo CSV.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.
  
  Ejemplo:
    >>> preliminar('ruta/al/archivo/csv')
    nombre,cajones,precio
    Lima,100,32.2
    Naranja,50,91.1
    Caqui,150,103.44
  """
  print('== Datos del archivo ==')
  try:
    with open(nombre_archivo, 'rt') as archivo:
      # leer el archivo entero es util con archivos chicos
      # data = archivo.read()
      # print(data)
      # es mejor usar un 'for' para controlar
      # cuantas lineas se quieren ver
      for linea in archivo:
        print(linea, end='')
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

def preliminar_dos(nombre_archivo):
  """Abrir y leer datos de un archivo CSV.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> preliminar_dos('ruta/al/archivo/csv')
    Headers
    ['nombre', 'cajones', 'precio']
    Datos
    ['Lima', '100', '32.2']
    ['Naranja', '50', '91.1']
    ['Caqui', '150', '103.44']
  """
  print('\n== Datos del archivo dos ==')
  try:
    archivo = open(nombre_archivo, 'rt')
    headers = next(archivo).split(',')
    print('Headers')
    print(headers)
    print('Datos')
    for linea in archivo:
      fila = linea.split(',')
      print(fila)
    archivo.close()
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

"""
2.2
Las columnas en `camion.csv` corresponden a un nombre de fruta,
una cantidad de cajones cargados en el camión, y un precio de compra
por cada cajón de ese grupo. Escribí un programa llamado
`costo_camion.py` que abra el archivo, lea las líneas, y calcule el
precio pagado por los cajones cargados en el camión.
Ver archivo <costo_camion.py>
"""

"""
2.3
El archivo `Data/precios.csv` contiene una serie de líneas con
precios de venta de cajones en el mercado al que va el camión.
Escribí un código que abra el archivo `Data/precios.csv`, busque
el precio de la naranja y lo imprima en pantalla.
'El precio de la naranja es: $106.28'
"""
def precio_naranja(nombre_archivo):
  """Abrir y leer datos de un archivo CSV.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> precio_naranja('ruta/al/archivo/csv')
    'El precio de la naranja es: $106.28'
  """
  print('\n== Precio de la naranja ==')
  precio = 0
  try:
    archivo = open(nombre_archivo, 'rt', encoding='utf8')
    for linea in archivo:
      fila = linea.split(',')
      producto = fila[0].lower()
      if (producto == 'naranja'):
        precio = float(fila[1])
        # evito seguir iterando innecesariamente
        break
    archivo.close()
  except FileNotFoundError:
    print('No existe el archivo o carpeta')
  print(f'El precio de la naranja es: ${precio}')

"""
2.4
¿Que pasaría si quisiéramos leer un archivo comprimido con gzip, por
ejemplo? La función primitiva de Python `open()` no hace esa tarea.
Pero hay un módulo de la biblioteca de Python llamado `gzip` que lee 
archivos comprimidos.
"""
def abrir_gzip(nombre_archivo):
  """Abrir y leer datos de un archivo comprimido CSV.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> abrir_gzip('ruta/al/archivo/comprimido/csv')
    nombre,cajones,precio
    Lima,100,32.2
    Naranja,50,91.1
    Caqui,150,103.44
  """
  print('\n== Abrir gzip ==')
  try:
    with gzip.open(nombre_archivo, 'rt') as archivo:
      for linea in archivo:
        print(linea, end='')
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

#
preliminar('../Data/camion.csv')
preliminar_dos('../Data/camion.csv')
precio_naranja('../Data/precios.csv')
abrir_gzip('../Data/camion.csv.gz')
