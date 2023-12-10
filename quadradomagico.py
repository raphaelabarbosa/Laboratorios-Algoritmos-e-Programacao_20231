def quadradomagico(m):
  #soma linhas
  somal = [] 
  for a in range(len(m)):
    somal1 = 0
    for b in range(len(m[a])):
      somal1 += m[a][b]
    somal.append(somal1)
  #soma colunas
  somac = []
  for a in range(len(m)):
    somac1 = 0
    for b in range(len(m[a])):
      somac1 += m[b][a]
    somac.append(somac1)
  #soma diagonal principal
  somadp = 0
  for a in range(len(m)):
    somadp += m[a][a]
  #soma diagonal secundária
  somads = 0
  for a in range(len(m)):
    somads += m[a][(len(m)-a - 1)]
  
  if sum(somal)/len(somal) == sum(somac)/len(somac) == somadp == somads:
    return True
  else:
    return False
matriz = eval(input())
print(quadradomagico(matriz))
