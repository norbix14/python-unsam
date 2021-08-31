import csv
from pprint import pprint

######################################################################

"""
4.4
Objetos.
"""

"""
4.12
Datos de primera clase.
"""

"""
4.13
Diccionarios.
"""
def diccionarios():
  try:
    camion = []
    with open('../Data/camion.csv', 'rt') as archivo:
      rows = csv.reader(archivo)
      headers = next(rows)
      types = [str, int, float]
      for row in rows:
        diccionario = {
          name: func(val)
          for name, func, val in zip(headers, types, row)
        }
        camion.append(diccionario)
    return camion
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

"""
4.14
Fijando ideas.
"""
def fijando_ideas():
  try:
    stocks = []
    with open('../Data/dowstocks.csv', 'rt') as archivo:
      rows = csv.reader(archivo)
      headers = next(rows)
      types = [str, float, str, str, float, float, float, float, int]
      for i, row in enumerate(rows):
        if (i == 2):
          break
        converted = [
          func(val)
          for func, val in zip(types, row)
        ]
        record = dict(zip(headers, converted))
        stocks.append(record)
    return stocks
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#
if __name__ == '__main__':
  pprint(diccionarios())
  pprint(fijando_ideas())
