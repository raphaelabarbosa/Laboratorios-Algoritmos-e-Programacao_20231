#Lab 9.3
class Polinomio:
  #Representa um polinomio de uma variavel.
  
    def __init__(self, coeficientes=[]):
        #Construtor: Recebe uma lista com os coeficientes posicionados no index de seu expoente. Forma um dicionário onde as chaves são os expoentes e os valores os coeficientes correspondentes.
        if type(coeficientes) is dict:
            self.pl = coeficientes
        else:
            self.pl = {}
        for i in range(len(coeficientes)):
            self.pl [i] = coeficientes[i]

    def grau (self):
        #Retorna o grau do polinomio.
        graup = 0
        for i in self.pl.keys():
            if i > graup:
                graup = i
        return graup
        
    def chave_ (self,p):
        # Retorna um set com a uniao das chaves de dois polinomios. (expoentes)
        chaves = set()
        for i in self.pl.keys():
            chaves.add(i)
        for i in p.keys():
            chaves.add(i)
        return chaves
 
    def __setitem__(self, grau, coeficiente):
        #Altera o coeficiente para o termo do expoente (grau) dado.
        self.pl[grau] = coeficiente
    
    def __getitem__(self,grau):
        #Retorna o coeficiente para o expoente (grau) dado.
        if grau in self.pl:
            return self.pl[grau]
        else:
            return 0
    
    def __mul__(self,p):
        #Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio).
        pf = {}
        x = p.pl
        for i in self.pl.keys():
            for j in x.keys():
                if i+j in pf:pf[i+j] = (self.pl[i]*x[j])+pf[i+j]   
                else: pf[i+j] = (self.pl[i]*x[j])
        return Polinomio(pf)
    
    def __add__(self,p):
        #Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio).
        pf = {}
        x = p.pl
        chaves = self.chave_(x)
        for i in chaves:
            if i in self.pl and i in x: pf[i] = self.pl[i]+x[i]
            elif i in self.pl: pf[i] = self.pl[i]
            else: pf[i] = x[i] 
            return Polinomio(pf)
     
    def __sub__(self,p):
        #Retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio).
        pf = {}
        x = p.pl
        chaves = self.chave_(x)
        for i in chaves:
            if i in self.pl and i in x: pf[i] = self.pl[i] - x [i]
            elif i in self.pl: pf[i] = self.pl[i]
            else: pf[i] = -(x[i])
            return Polinomio(pf)
    
    def avalia (self,x):
        #Retorna a avaliacao do polinomio avaliado em x.
        resultado = 0
        for i in self.pl.keys():
            if self.pl[i] != 0: resultado += self.pl[i]*(x**i)
        return resultado

    def derivada(self):
        #Retorna a sua derivada do polinomio.
        derivada = {}
        for i in self.pl.keys():
            derivada[i-1] = i*self.pl[i]
        return Polinomio(derivada)
      
    def raizaprox(self,p,n):
    #Retorna aproximação da raiz x do polinomio e f(x) (Em uma tupla (f(x),x) pelo método de Newton-Raphson em n iterações.
      for i in range(n):
        fp = self.avalia(p)
        if fp == 0: break
        dp = self.derivada(p)
        try:
          p = p - (fp/dp)
        except ZeroDivisionError: return 'Abortado'
      return "(%.2f,%.2f)" %(self.avalia(p),p)
  
    def integralQ(self,a,b,n):
        #Retorna a integral de um polinomio pela regra de Newton-Cotes.
        intervalo = (b-a)/n
        integral = 0
        i = a
        j = a + intervalo
        while j <= b:
            integral += (j-i) * self.avalia((i+j)/2)
            i += intervalo
            j += intervalo
        return(integral)

    def integralT(self,a,b,n):
        #Retorna a integral de um polinomio pela regra Trapezoidal.
        intervalo = (b-a)/n
        integral = 0
        i = a
        j = a + intervalo
        while j <= b:
            integral += (j-i) * ((self.avalia(i) + self.avalia(j))/2)
            i += intervalo
            j += intervalo
        return(integral)
