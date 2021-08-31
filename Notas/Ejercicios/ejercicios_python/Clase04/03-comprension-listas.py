import csv
from pprint import pprint

######################################################################

"""
4.3
"""

"""
4.7
Comprension de listas.
Probar un par de comprension de listas para familiarizarse con la
sintaxis.
"""

"""
4.8
Reduccion de secuencias.
Calcular el costo total de la carga del camion en un solo comando.
"""

"""
4.9
Consultas de datos.
La forma de escribir estas consultas en un analogo a las consultas
a una base de datos.
"""

"""
4.10
Extraccion de datos.
"""

"""
4.11
Extraer datos de un archivo CSV.
"""
def extraer_datos_csv(nombre_archivo = '../Data/fecha_camion.csv'):
  """Extraer datos de un archivo CSV.

  Ejercicio 4.11 de Clase04 - 03_Comprension_Listas.
  """
  try:
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
      rows = csv.reader(f)
      headers = next(rows)
      select = ['nombre', 'cajones', 'precio']
      indices = [
        headers.index(ncolumna)
        for ncolumna in select
      ]
      camion = [
        {
          ncolumna: row[index]
          for ncolumna, index in zip(select, indices)
        }
        for row in rows
      ]
      return camion
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#
if __name__ == '__main__':
  # 4.11
  camion = extraer_datos_csv()
  pprint(camion)
