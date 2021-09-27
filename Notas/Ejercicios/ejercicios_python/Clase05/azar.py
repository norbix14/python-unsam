#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# azar.py

import random

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
def main():
  #n = 10000
  c = cumple()
  print(c)

#%%
if __name__ == '__main__':
  main()
