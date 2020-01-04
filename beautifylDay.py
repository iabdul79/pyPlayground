def beautifulDays(i, j, k):
  c=0
  for _i in range(i,j+1):
    if abs(_i - rev(_i))%k == 0:
      c+=1
  return c

def rev(n):
  return int(str(n)[::-1])

print(beautifulDays(20, 23, 6))
  