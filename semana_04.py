# %%
import numpy as np
import csv
from collections import Counter
from collections import defaultdict

# %%
def arboles_parque(nombre_archivo, nombre_parque):
  list_dic=[]
  with open(nombre_archivo, 'r', encoding="utf-8") as arbolado:
    lineas=arbolado.readlines()
    encabezado=lineas[0].strip().split(',')

    for linea in lineas[1:]:
      val= linea.strip().split(',')
      filaarbolado=dict(zip(encabezado,val))

      if filaarbolado['espacio_ve'].lower()==nombre_parque.lower():
        list_dic.append(filaarbolado)
  return list_dic

# %%
def arbol_mas_popular(nombre_parque):
  list_arbol= arboles_parque(nombre_archivo, nombre_parque)
  nombres_comunes=[arbol['nombre_com']for arbol in list_arbol]
  cont = Counter(nombres_comunes)
  mas_comun=cont.most_common(1)

  if mas_comun:
    return mas_comun[0][0]
  else:
    return None
  return mas_comun

# %%
def n_mas_altos(nombre_archivo,  nombre_parque, n):
  list_arbol= arboles_parque(nombre_archivo, nombre_parque)
  arboles_altos= [(arbol['nombre_com'], int(arbol['altura_tot']))for arbol in list_arbol]
  arboles_altos.sort(key=lambda x: x[1], reverse=True)
  return arboles_altos[:n]

# %%
def altura_promedio(nombre_archivo, nombre_parque, especie):
  list_arbol=arboles_parque(nombre_archivo, nombre_parque)
  alturas=[int(arbol['altura_tot'])for arbol in list_arbol if arbol['nombre_com'].lower()==especie.lower()]
  if alturas:
    return sum(alturas) / len(alturas)
  else:
    return 0

# %%
def parque_mas_arboles(nombre_archivo):
  cont_parq={}

  with open(nombre_archivo, 'r', encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
      parque=fila['espacio_ve']
      if parque not in ['S/D','']:
        cont_parq[parque] = cont_parq.get(parque, 0) + 1
  if cont_parq:
    max_valor=max(cont_parq.values())
    parque_max = [parque for parque, cantidad in cont_parq.items() if cantidad == max_valor]

  return parque_max

# %%
def parque_mas_altos_arboles(nombre_archivo):
  suma_altura = defaultdict(float)
  cont_arbol = defaultdict(int)

  with open(nombre_archivo, 'r' , encoding="utf-8") as f:
    lector=csv.DictReader(f)
    for fila in lector:
      try:
        parque=fila['espacio_ve']
        altura=float(fila['altura_tot'])
        suma_altura[parque]+=altura
        cont_arbol[parque]+=1
      except ValueError:
        continue

  prom={parque:suma_altura[parque]/cont_arbol[parque] for parque in suma_altura}
  max_promedio = max(prom.values())
  return [parque for parque, promedio in prom.items() if promedio == max_promedio]

# %%
def parque_mas_variado(nombre_archivo):
  espec_parq=defaultdict(set)

  with open(nombre_archivo, 'r', encoding="utf-8") as f:
    lector=csv.DictReader(f)
    for fila in lector:
      parque=fila['espacio_ve']
      especie=fila['nombre_com']
      if parque != 'S/D' and especie != 'S/D':
        espec_parq[parque].add(especie)
  max_variedad=max(len(especies) for especies in espec_parq.values())
  return [parque for parque, especies in espec_parq.items()if len(especies)==max_variedad]

# %%
def especie_frecuente(nombre_archivo):
  cont=Counter()
  with open(nombre_archivo, 'r', encoding="utf-8") as f:
    lector=csv.DictReader(f)
    for fila in lector:
      especie=fila['nombre_com']
      if especie != 'S/D':
        cont[especie]+=1
  return cont.most_common(1)[0]

# %%
def rel_exot_autoc(nombre_archivo):
  cant_exot=0
  cant_autoc=0

  with open(nombre_archivo, 'r', encoding="utf-8") as f:
    lector=csv.DictReader(f)
    for fila in lector:
      origen=fila['origen'].lower()
      if'exótico' in origen:
        cant_exot += 1
      elif 'nativo/autóctono' in origen:
        cant_autoc += 1
  return cant_exot/cant_autoc


