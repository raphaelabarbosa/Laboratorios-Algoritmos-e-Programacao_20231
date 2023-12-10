def BuscaBinaria(v,x):
  i = 0
  j = len(v)-1
  def a(v,x,i,j):
    if i > j: return -1
    m = round((i+j)/2)
    if v[m] < x:
      i = m + 1
      return a(v,x,i,j)
    elif v[m] > x:
      j = m - 1
      return a(v,x,i,j)
    else:
      return m
  return a(v,x,i,j)
vetor = eval(input())
numero = int(input())
print(BuscaBinaria(vetor,numero))
