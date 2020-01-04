def permutationEquation(p):
  siz = len(p)
  r=[0]*siz
  l=[0]*siz
  i=0
  while i<siz:
    r[p[i]-1] = i+1
    i+=1
  i=1
  while i<=siz:
    l[i-1] = r[r[i-1]-1]
    i+=1
  return l

print(permutationEquation([4, 3, 5, 1, 2]))