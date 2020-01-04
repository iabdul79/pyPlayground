def viralAdvertising(n):
  p=5
  c=0
  for n in range(n):
    l=int(p/2)
    c=c+l
    p=l*3
  return c

print(viralAdvertising(3))