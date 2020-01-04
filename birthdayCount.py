def birthday(s, d, m):
  if len(s) < m:
    return 0
  sPtr = nPtr = 0
  result = 0
  count = 0
  while nPtr < m:
    result = result + s[nPtr]
    nPtr = nPtr + 1
  count = count +1 if result == d else count
  while nPtr < len(s):
    result = result - s[sPtr]
    result = result + s[nPtr]
    if result == d:
      count = count+1
    sPtr = sPtr+1
    nPtr = nPtr+1
  return count

print(birthday([4, 5, 4, 5, 1, 2, 1, 4, 3, 2, 4, 4, 3, 5, 2, 2, 5, 4, 3, 2, 3, 5, 2, 1, 5, 2, 3, 1, 2, 3, 3, 1, 2, 5], 18, 6))