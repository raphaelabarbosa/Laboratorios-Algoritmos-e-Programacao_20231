class Matriz:
    def __init__(self,n,m,v):
        self.n = n
        self.m = m
        if len(v) == n:
            self.v = v
        else:
            self.v = v
            self.v = self.matriz(n,m,v)

    def matriz(self,n,m,v):
        M = []
        for i in range(self.n):
            M += [self.v[i*self.m:((i+1)*self.m)]]
        return M

    def __add__(self,other):
        vetor = []
        for a in range(self.n):
            vetord = []
            for b in range(self.m):
                vetord.append(self.v[a][b]+ other.v[a][b])
            vetor.append(vetord)
        return Matriz(other.n,other.m,vetor)

    def __sub__(self,other):
        vetor = []
        for a in range(self.n):
            vetord = []
            for b in range(self.m):
                vetord.append(self.v[a][b]-other.v[a][b])
            vetor.append(vetord)
        return Matriz(other.n,other.m,vetor)

    def __mul__(self,other):
        vetor =[]
        for i in range(self.n):
            vetor.append([0]*other.m)
        for a in range(self.n):
            for b in range(other.m):
                for c in range(self.n):
                    vetor[a][b] += self.v[a][c]*other.v[c][b]
        return Matriz(other.n,other.m,vetor)
      
    def __repr__(self):
        return str(self.v)


entrada = input()
a = ''
b = ''
operador = ''
for i in entrada:
  if (i == "+" or i == "-" or i == "*") and b == "":
    operador  += i
  elif operador == '':
    a += i
  elif  operador != '':
    b += i
print(a,b,operador)
a = "Matriz"+a
b = "Matriz"+b
resultado = eval(a+operador+b)
print (resultado)
