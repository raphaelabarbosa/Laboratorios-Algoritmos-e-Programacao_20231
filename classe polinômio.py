class Polinomio:
  #"Representa um polinomio de uma variavel"
  
  def __init__(self, coeficientes=[]):
    #"Construtor, onde a lista coeficientes contem os coeficientes para os termos de grau 0, grau 1, etc
    if type(coeficientes) is dict:
      self.pl = coeficientes
    else:
      self.pl = {}
      for i in range(len(coeficientes)):
        self.pl [i] = coeficientes[i]

  def grau (self):
    #"Retorna o grau do polinomio"
    graup = 0
    for i in self.pl.keys():
      if i > graup:
        graup = i
    return graup
        
  def chave_ (self,p):
    chaves = set()
    for i in self.pl.keys():
      chaves.add(i)
    for i in p.keys():
      chaves.add(i)
    return chaves
 
  def __setitem__(self, grau, coeficiente):
    #"Altera o coeficiente para o termo do grau dado"
      self.pl[grau] = coeficiente
    
  def __getitem__(self,grau):
    #"Retorna o coeficiente para o grau dado"
    if grau in self.pl:
      return self.pl[grau]
    else:
      return 0
    
  def __mul__(self,p):
    #"Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio
    pf = {}
    x = p.pl
    for i in self.pl.keys():
      for j in x.keys():
        if i+j in pf:
         pf[i+j] = (self.pl[i]*x[j])+pf[i+j]
        else:
          pf[i+j] = (self.pl[i]*x[j])
    return Polinomio(pf)
    
  def __add__(self,p):
    #"Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio)
    pf = {}
    x = p.pl
    chaves = self.chave_(x)
    for i in chaves:
      if i in self.pl and i in x:
        pf[i] = self.pl[i]+x[i]
      elif i in self.pl:
        pf[i] = self.pl[i]
      else:
        pf[i] = x[i]
    return Polinomio(pf)
     
  def __sub__(self,p):
    #"retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio)"
    pf = {}
    x = p.pl
    chaves = self.chave_(x)
    for i in chaves:
      if i in self.pl and i in x:
        pf[i] = self.pl[i] - x [i]
      elif i in self.pl:
        pf[i] = self.pl[i]
      else:
        pf[i] = -(x[i])
    return Polinomio(pf)
    
  def avalia (self,x):
    #"Retorna a avaliacao do polinomio avaliado em x."
    resultado = 0
    for i in self.pl.keys():
      resultado += self.pl[i]*(x**i)
    return resultado

p = Polinomio(eval(input()))
q = Polinomio(eval(input()))
x = eval(input())
print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))
