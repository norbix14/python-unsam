#!/usr/bin/env python3
# tests.py

import repaso

######################################################################

# 6.1 - repaso de temas pasados

#%% 6.1
def test_propagar_al_vecino():
  r = repaso
  r.propagar_61([0,0,0,0,1])
  r.propagar_61([0,0,1,0,0])
  r.propagar_61([1,0,0,0,0])
  return None

#%% 6.2
def test_propagar_auto_fantastico():
  r = repaso
  l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
  print('Estado original:', l)
  print('Propagando...')
  lp = r.propagar_62(l)
  print('Estado original:', l)
  print('Estado propagado:', lp)
  return None

#%% 6.3
def test_propagar_cadenas():
  r = repaso
  l2 = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
  lp2 = r.propagar_63(l2)
  print('Estado original:', l2)
  print('Estado propagado:', lp2)
  return None
