def circularArrayRotation(a, k, queries):
  size = len(a)
  y = k%size
  z = y if y==size else size-y
  r=[]
  for q in queries:
    x=z+q
    i=x if x<size else x-size
    r.append(a[i])
  return r

print(circularArrayRotation([1, 2, 3], 2, [0,1,2]))
