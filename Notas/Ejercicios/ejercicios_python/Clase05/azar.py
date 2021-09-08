#!/usr/bin/env python3
# azar.py

import random
from pprint import pprint

######################################################################

# 5.3 - Cocumpleaños

#%% cocumpleaños
def cumple():
  """Ejercicio 5.3 - Cocumpleaños"""
  init = 1
  people = 30
  year = 365
  birthday = [
    random.randint(init, year)
    for _ in range(people)
  ]
  #person = [i for i in range(1, people + 1)]
  #values = [(p, b) for p, b in zip(person, birthday)]
  #return values
  return birthday

#%%
if __name__ == '__main__':
  n = 10000
  c = cumple()
  print(c)
