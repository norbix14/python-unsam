######################################################################

"""
3.12
Formato de numeros.
"""
def formato_numeros():
  value = 42863.1
  print('Valor tal cual:', value)
  print('Valor formateado 1')
  print(f'{value:0.4f}')
  print('Valor formateado 2')
  print(f'{value:>16.2f}')
  print('Valor formateado 3')
  print(f'{value:<16.2f}')
  print('Valor formateado 4')
  print(f'{value:*>16,.2f}')
  print('Valor formateado 5')
  print('%0.4f' % value)
  print('Valor formateado 6')
  print('%16.2f' % value)

"""
3.13
Recolectar datos.
En el [Ejercicio 2.18], escribiste un programa llamado `informe.py`
que calculaba las ganancias o pérdidas de un camión que compra a
productores y vende en el mercado. Copiá su contenido en un archivo
`tabla_informe.py`.
Ver archivo <tabla_informe.py>.
"""

"""
3.14
Imprimir una tabla con formato.
Ver archivo <tabla_informe.py>.
"""

"""
3.15
Agregar encabezados.
Ver archivo <tabla_informe.py>.
"""

"""
3.16
Un desafio de formato.
Ver archivo <tabla_informe.py>.
"""

"""
3.17
Tablas de multiplicar.
Ver archivo <tablamult.py>.
"""

#
formato_numeros()
