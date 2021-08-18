import csv

######################################################################

"""
Tipos de datos.
"""

"""
2.11
Tuplas.
"""
def tuplas(nombre_archivo):
  print('\n== Tuplas ==')
  try:
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    next(filas) # header
    info = next(filas) # pedido
    t = (info[0], int(info[1]), float(info[2]))
    nombre, cajones, precio = t
    cost = cajones * precio
    archivo.close()
    print(f'Pedido: {cajones} cajones de {nombre} a ' +
          f'${precio} pesos cada cajon')
    print(f'Costo total: ${cost:0.2f} pesos')
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

"""
2.12
Diccionarios como estructuras de datos.
"""
def diccionarios(nombre_archivo):
  print('\n== Diccionarios ==')
  try:
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    next(filas) # header
    info = next(filas) # pedido
    d = {
      'nombre': info[0],
      'cajones': int(info[1]),
      'precio': float(info[2])
    }
    archivo.close()
    cost = d['cajones'] * d['precio']
    print(f"Pedido: {d['cajones']} cajones de {d['nombre']} a " +
          f"${d['precio']} pesos cada cajon")
    print(f"Costo total: ${cost:0.2f} pesos")
    d['fecha'] = (26, 7, 2021)
    d['cuenta'] = 'norberto'
    print(f'\n{d}')
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

"""
2.13
Mas operaciones con diccionarios.
Si usas el comando 'for' para iterar sobre el diccionario,
obtenes las claves.
"""
def bucle_for_diccionario(nombre_archivo):
  print('\n== Iterar diccionario ==')
  try:
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    next(filas) # headers
    info = next(filas) # pedido
    d = {
      'nombre': info[0],
      'cajones': info[1],
      'precio': info[2],
      'fecha': (26, 7, 2021),
      'cuenta': 'norberto'
    }
    archivo.close()
    for k in d:
      print(f'{k} = {d[k]}')
    print('\n')
    for k, v in d.items():
      print(f'{k} = {v}')
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

"""
2.14
Diccionario geringoso.
Construir una función que, a partir de una lista de palabras, 
devuelva un diccionario geringoso. Las claves del diccionario deben
ser las palabras de la lista y los valores deben ser sus traducciones
al geringoso (como en el [Ejercicio 1.18]). 
Probar la función para la lista `['banana', 'manzana', 'mandarina']`.
Ver archivo <diccionario_geringoso.py>
"""

# 2.11
tuplas('')
# 2.12
diccionarios('')
# 2.13
bucle_for_diccionario('')
