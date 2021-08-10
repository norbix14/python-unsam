#!/usr/bin/env python3
# inclusive.py

######################################################################
"""
@author: Norberto Fabrizio
"""

#%%
# 1.29

def inclusive(frase):
  """Traducir a lenguaje inclusivo.

  Parametros:
    `frase` (str): cadena a traducir.

  Ejemplo:
  >>> traduccion = inclusive('todos somos programadores')
  >>> print(traduccion)
  'todes somes programadores'
  """
  palabras = frase.strip().split(' ')
  traduccion = ''
  lista_inclusiva = []
  for i in range(len(palabras)):
    palabra = palabras[i].lower()
    long_palabra = len(palabra)
    inclusive = ''
    for j in range(long_palabra):
      letra = palabra[j]
      aux = letra
      if (j == long_palabra - 2):
        if (letra == 'o'):
          aux = 'e'
        else:
          aux = letra
      inclusive += aux
    lista_inclusiva.append(inclusive)
  traduccion = ' '.join(lista_inclusiva)
  return traduccion

#%%
a = 'todos somos programadores'
b = 'los hermanos sean unidos porque esa es la ley primera'
c = '¿como transmitir a los otros el infinito Aleph?'
d = 'todos, tu tambien'

#%%
print(inclusive(a))
print(inclusive(b))
print(inclusive(c))
print(inclusive(d))
