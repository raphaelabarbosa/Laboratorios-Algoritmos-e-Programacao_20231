fibonacci = [0]
n = int(input())
if n > 0:
  fibonacci += [1]
  while fibonacci[-1] + fibonacci[-2] <= n:
    fibonacci += [fibonacci[-1] + fibonacci[-2]]
print(fibonacci)
print(sum(fibonacci))
