# %%
import random

# %%
def crear_album(figus_total):
  return[0]* figus_total

# %%
def album_incompleto(A):
  return 0 in A

# %%
def comprar_figu(figus_total):
  return random.randint(0,figus_total-1)

# %%
def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    compra=0
    while album_incompleto(album):
      figu = comprar_figu(figus_total)
      album[figu]+= 1
      compra+=1
    return compra

# %%
def albumde6figus():
  resultado=[cuantas_figus(6) for _ in range(1000)]
  promedio=sum(resultado) / len(resultado)
  return promedio

# %%
def experimento_figus(n_repeticiones, figus_total):
  result=[cuantas_figus(figus_total)for _ in range(n_repeticiones)]
  promedio=sum(result) / len(result)
  return promedio

# %%
def comprar_paquete(figus_total, figusenpaq=5):
  return [random.randint(0, figus_total-1) for _ in range(figusenpaq)]

# %%
def cuantos_paquetes(figus_total, figusenpaq=5):
    album=crear_album(figus_total)
    paq_compr=0
    while album_incompleto(album):
      paquete = comprar_paquete(figus_total,figusenpaq)
      for figu in paquete:
        album[figu]+= 1
      paq_compr+=1
    return paq_compr

# %%
def experimento_paquetes(n_repeticiones, figus_total, figusenpaq):
  result=[cuantos_paquetes(figus_total, figusenpaq)for _ in range(n_repeticiones)]
  promedio=sum(result) / len(result)
  return promedio


