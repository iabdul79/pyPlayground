def arrayManipulation(n, queries):
  a=[0]*(n+1)
  maxV=0
  x=0
  for i in queries:
    k=i[0]
    l=i[1]
    m=i[2]
    a[k]+=m
    if l+1<n:
      a[l+1]-=m
  for i in a:
    x=x+i
    maxV = max(maxV, x)
  return maxV


print(arrayManipulation(4, [
[2, 3, 603],
[1, 1, 286],
[4, 4, 882],
]))