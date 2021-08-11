#!/usr/bin/env python3
# hipoteca.py

######################################################################
"""
@author: Norberto Fabrizio
"""

#%%
# 1.10

def hipoteca(saldo, tasa, mensual):
  """Mostrar una tabla informativa con datos de la hipoteca.

  Parametros:
    `saldo` (int): saldo del credito.
    `tasa` (float): tasa de interes.
    `mensual` (float): pago mensual.

  Ejemplo:
    >>> saldo = 500000.0
    >>> tasa = 0.05
    >>> mensual = 2684.11
    >>> hipoteca(saldo, tasa, mensual)
    '==== Tabla informativa ===='
    'Cuota - Total pagado - Saldo restante'
    1  2684.11 499399.22
    2  5368.22 498795.94
    3  8052.33 498190.15
    4 10736.44 497581.83
    5 13420.55 496970.98
    ...
    306 869337.66 8784.87
    307 872021.77 6137.36
    308 874705.88 3478.83
    309 877389.99  809.21
    310 878202.57    0.00
    'Total pagado: $878202.57'
    'Meses pagados: 310'
    'Pagos realizados: 310'
    'Meses adelantados: 48'
  """
  pago_extra_mes_comienzo = 61
  pago_extra_mes_fin = 108
  adelanto = 1000
  total_pagado = 0.0
  meses_pagados = 0
  pagos_realizados = 0
  meses_pagados = 0
  meses_adelantados = 0
  print('==== Tabla informativa ====')
  print('Cuota - Total pagado - Saldo restante')
  while (saldo > 0):
    meses_pagados += 1
    pagos_realizados += 1
    # >>> correccion de saldo ...
    a_pagar = 0
    if (meses_pagados >= pago_extra_mes_comienzo and 
        meses_pagados <= pago_extra_mes_fin):
      pago_mensual_especial = adelanto + mensual
      a_pagar = pago_mensual_especial
      meses_adelantados += 1
    else:
      a_pagar = mensual
    if (saldo * (1 + tasa / 12) < a_pagar):
      a_pagar = saldo * (1 + tasa / 12)
    saldo = saldo * (1 + tasa / 12) - a_pagar
    total_pagado += a_pagar
    # ... copiada de la clase de consulta <<<
    print(f'{meses_pagados:10d}' + 
          f'{round(total_pagado, 4):10.2f}' +
          f'{round(saldo, 4):10.2f}')
  print('\n')
  print(f'Total pagado: ${round(total_pagado, 2):0.2f}')
  print(f'Meses pagados: {meses_pagados}')
  print(f'Pagos realizados: {pagos_realizados}')
  print(f'Meses adelantados: {meses_adelantados}')

#%%
saldo = 500000.0
tasa = 0.05
mensual = 2684.11

#%%
hipoteca(saldo, tasa, mensual)
