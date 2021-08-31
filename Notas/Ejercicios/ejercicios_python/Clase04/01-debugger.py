import csv
from pprint import pprint

######################################################################

"""
4.1
Debuggear programas
"""

"""
4.1
Debugger
Correr codigo en IDE.
"""
def invertir_lista(lista):
  """Recibe una lista y la devuelve invertida."""
  invertida = []
  i = len(lista)
  while i > 0:
    i -= 1
    invertida.append(lista.pop(i))
  return invertida

"""
4.2
Mas debugger
Usar debugger para analizar el codigo.
"""
def leer_camion(nombre_archivo):
  """Esta funcion tiene un error. Hay que mover
  la definicion de registro a dentro del loop for
  asi comienza vacio y se va llenando con los datos
  correctos."""
  camion = []
  registro = {}
  with open(nombre_archivo, 'rt') as archivo:
    filas = csv.reader(archivo)
    encabezado = next(filas)
    for fila in filas:
      registro[encabezado[0]] = fila[0]
      registro[encabezado[1]] = int(fila[1])
      registro[encabezado[2]] = float(fila[2])
      camion.append(registro)
  return camion

#
if __name__ == '__main__':
  # 4.1
  lista = [1, 2, 3, 4, 5, 6]
  inversa = invertir_lista(lista)
  print('Original')
  print(lista)
  print('Inversa')
  print(inversa)
  # 4.2
  camion = leer_camion('../Data/camion.csv')
  pprint(camion)
