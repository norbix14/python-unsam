######################################################################

"""
2.5
Probar primero definir una funcion simple.
"""

"""
2.6
Transformá el programa <costo_camion.py> en una función 
'costo_camion(nombre_archivo)'.
Esta función recibe un nombre de archivo como entrada, lee la
información sobre los cajones que cargó el camión y devuelve el
costo de la carga de frutas como una variable de punto flotante.
"""

"""
2.7
A partir de lo que hiciste en el [Ejercicio 2.3], escribí una función
'buscar_precio(fruta)' que busque en archivo '../Data/precios.csv'
el precio de determinada fruta (o verdura) y lo imprima en pantalla.
Si la fruta no figura en el listado de precios, debe imprimir un
mensaje que lo indique.
Ver archivo <buscar_precio.py>.
"""

"""
2.8
Administracion de errores.
try, except.
"""
def preguntar_edad(nombre):
  """Preguntar edad al usuario. Si la edad no es valida
  (no es un entero), una excepcion es arrojada.

  Parametros:
    `nombre` (str): nombre del usuario.

  Ejemplo:
    >>> edad = preguntar_edad('norberto')
    'Ingresa tu edad norberto:' 
  """
  edad = int(input(f'Ingresa tu edad {nombre}: '))
  if (edad < 0):
    raise ValueError('La edad no puede ser negativa')
  return edad

def ver_edades():
  """Ver las edades de los usuarios.

  Ejemplo:
    >>> ver_edades()
    'Ingresa tu edad [usuario]:'
    '[usuario] tiene [edad] años'
  """
  nombres = ['fernando', 'juan', 'pablo']
  for nombre in nombres:
    try:
      edad = preguntar_edad(nombre)
      print(f'{nombre} tiene {edad} años')
    except ValueError as e:
      print(f'{nombre} no ingreso una edad valida')
      print(e)

"""
2.9
Funciones de la biblioteca.
Python viene con una gran biblioteca estándar de funciones útiles.
En este caso el módulo `csv` podría venirnos muy bien.
Podés usarlo cada vez que tengas que leer archivos CSV.
Una cosa buena que tiene el módulo `csv` es que maneja solo una
gran variedad de detalles de bajo nivel como el problema de las
comillas, o la separación con comas de los datos.
"""

"""
2.10
Ejecucion desde la linea de comandos con parametros.
Una posibilidad es pasarle al programa el nombre del archivo que
querés procesar como un parámetro cuando lo llamás desde la línea
de comandos.
Ver archivo <camion_commandline.py>.
"""

#
ver_edades()
