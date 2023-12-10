class Vetor(list):     
  def mdc(v):
    def tratamento(v):
      if len(v) == 1:
        return ()
      v1 = list(v)
      vf = []
      for i in v1:
        i =str(i)
        if i.isnumeric() and int(i) not in vf: vf +=[int(i)]
        elif "." in i:
          ponto = i.index(".")
          if i[ponto+1:] == "0" and i[:ponto].isnumeric():
            n = int(i[:ponto])
            if n not in vf: vf +=[n]
      return vf

    def BuscaBinaria(v,x):
      i = 0
      j = len(v)-1
      def a(v,x,i,j):
        if i > j: return i
        m = round((i+j)/2)
        if v[m] < x:
          i = m + 1
          return a(v,x,i,j)
        elif v[m] > x:
          j = m - 1
          return a(v,x,i,j)
        else:
          return (m+1)
      return a(v,x,i,j)
  
    def ordenador(v):
      vetorf = []
      for x in v:
        a = BuscaBinaria(vetorf,x)
        vetorf[a:a] = [x]
      return tuple(vetorf)
    
    def divisores(n,i=1):
      if i>n:
        return {1}
      if n%i==0:
        return {i}.union(divisores (n,i+1))
      else:
        return divisores (n,i+1)
      
    def divcomum(vetor,m= set()):
      if len(vetor) < 2:
        return (ordenador(m))
      else:
        div=divisores(vetor[0]).intersection(divisores(vetor[1]))
        m.add(max(div))
        return divcomum(vetor[1:])
      
    if len(v) == 1:
        return ()
    else:
      vetor = tratamento(v)
      return divcomum(vetor)
      
entrada = Vetor(eval(input()))
print(entrada.mdc())
