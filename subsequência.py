vetor1 = eval(input())
vetor2 = eval(input())
verificador = []
for a in vetor1:
  for b in range(len(vetor2)):
    if a == vetor2[b]:
      verificador += [a]
      vetor2 = vetor2[b+1:]
      break
  if verificador == []:
    break
print(vetor1 == verificador)
