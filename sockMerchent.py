def sockMerchant(n, c):
  tot = 0
  d = {}
  for i in range(n):
    if c[i] in d:
      d.pop(c[i])
      tot += 1
    else:
      d[c[i]] = 1
  return tot

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))