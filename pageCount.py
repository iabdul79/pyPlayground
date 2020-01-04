def pageCount(n, p):
  k = n if n%2 else n+1 
  return int((k-p)/2) if k-p < p else int(p/2)

print(pageCount(10,5))