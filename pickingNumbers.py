def pickingNumbers(a):
  a.sort()
  s = []
  i=0
  t=0
  j = i+1
  while i < len(a):
    if j<len(a) and abs(a[j]-a[i]) <= 1:
      if t == 0:
        t+=1
      t+=1
      j+=1
      continue
    s.append(t)
    t = 0
    i+=1
    j=i+1
  return max(s)




print(pickingNumbers([1, 2, 2, 3, 1, 2]))