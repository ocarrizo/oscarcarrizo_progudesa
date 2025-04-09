# %%
def invertir_lista(lista):
  lista.reverse()
  return lista

# %%
def collatz(nro):
  cont = 1
  while nro!= 1:
    if nro %2 ==0:
      nro= nro // 2
    else:
      nro= nro*3 + 1
      cont +=1
  return cont

# %%
def contar_definiciones(d):
  for clave in d:
    d[clave] = len(d[clave])
  return d

# %%
def cantidad_de_claves_letra(dd,l):
  cont = 0
  for clave in dd:
    if clave[0] == l:
      cont +=1
  return cont

# %%
def propagación(L):
  for i in range(1,len(L)-1):
    if L[i] == 0:
      if L[i-1]==1 or L[i+1]==1:
        L[i]=1
  return L


