#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vida.py
"""
@author: Norberto Fabrizio
"""

from datetime import datetime, timedelta, date

# 8.2 - Manejo de fechas y horas

#%% 8.1 - segundos vividos hasta la fecha
def vida_en_segundos(fecha_nac):
  """Mostrar la cantidad de segundos vividos a partir de una fecha de
  nacimiento.

  Parametros:
    `fecha_nac` (str): fecha de nacimiento en formato `dd/mm/AAAA`.

  Ejemplo:
    >>> vida_en_segundos('25/07/1991')
    953115780.0

  Última actualización: 06-10-2021 10:30
  """
  try:
    hoy = datetime.now()
    nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    h = datetime(
      year=hoy.year,
      month=hoy.month,
      day=hoy.day,
      hour=hoy.hour,
      minute=hoy.minute
    )
    n = datetime(
      year=nac.year,
      month=nac.month,
      day=nac.day,
      hour=nac.hour,
      minute=nac.minute
    )
    f = h - n
    return f.total_seconds()
  except ValueError:
    print('Error. El formato adecuado es dd/mm/YYYY.')
    return 0.0

#%% 8.2 - cuantos dias faltan para la proxima primavera
def dias_para_proxima_primavera():
  """Calcular cuantos dias faltan para la proxima primavera."""
  hoy = datetime.now()
  h = datetime(year=hoy.year, month=hoy.month, day=hoy.day)
  p = datetime(year=hoy.year + 1, month=9, day=21)
  f = p - h
  return f.days

#%% 8.3 - fecha de reincorporacion
def reincorporacion(comienzo = '26/09/2020', duracion = 200):
  """Calcular fecha de reincorporacion luego de una licencia.

  Parametros:
    `comienzo` (str): fecha a partir de la cual comenzar a contar.
    `duracion` (int): duracion en dias

  Ejemplo:
    >>> reincorporacion(comienzo = '26/09/2020', duracion = 200)
    datetime.datetime(2021, 4, 14, 0, 0)

  Última actualización: 06-10-2021 10:00
  """
  try:
    lic = datetime.strptime(comienzo, '%d/%m/%Y')
    c = datetime(year=lic.year, month=lic.month, day=lic.day)
    days = timedelta(days=duracion)
    return c + days
  except ValueError:
    print('Error. El formato adecuado es dd/mm/YYYY.')
    return datetime.now()

#%% 8.4 - dias habiles entre fechas sin contar feriados
def dias_habiles(inicio, fin, feriados):
  """Calcular los dias habiles entre dos fechas dadas.

  Parametros:
    `inicio` (str): dia inicial.
    `fin` (str): dia final
    `feriados` (list): lista de feriados.

  Ejemplo:
    >>> dias_habiles('20/09/2020', '10/10/2020', ['12/10/2020', '23/11/2020'])

  Última actualización: 06-10-2021 11:30
  """
  # TODO: TERMINAR Y MEJORAR
  try:
    formato = '%d/%m/%Y'
    init = datetime.strptime(inicio, formato)
    end = datetime.strptime(fin, formato)
    dias_habiles = 0

    if feriados:
      todos_feriados = [datetime.strptime(f, formato) for f in feriados]
      dias_feriados = {f for f in todos_feriados}
      for i in range(1, 32):
        try:
          dia_actual = date(init.year, init.month, i)
        except ValueError:
          break
        if ((dia_actual.weekday() < 5) and (dia_actual not in dias_feriados)):
          dias_habiles += 1
    else:
      for i in range(1, 32):
        try:
          dia_actual = date(init.year, init.month, i)
        except ValueError:
          break
        if (dia_actual.weekday() < 5):
          dias_habiles += 1

    return dias_habiles
  except ValueError:
    print('Error. El formato adecuado es dd/mm/YYYY.')
    return 0

#%%
def main():
  feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
  print(dias_habiles('20/09/2020', '10/10/2020', []))
  print(dias_habiles('20/09/2020', '31/12/2020', feriados))

#%%
if __name__ == '__main__':
  main()
