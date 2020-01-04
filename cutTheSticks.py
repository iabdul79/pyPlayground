def cutTheSticks(arr):
  arr.sort()
  r=[]
  minA = arr[0]
  rmC = len(arr)
  ccount=0
  for i in arr:
    if minA == i:
      ccount+=1
      continue
    else:
      r.append(rmC)
      rmC-=ccount
      ccount=1
      minA=i
  r.append(rmC)
  return r

print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))

