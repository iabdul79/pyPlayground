def beautifulTriplets(d, arr):
  sPtr = 0
  lenA = len(arr)
  i=sPtr
  rCount=0
  count=1
  while i<lenA:
    j=i+1
    while j < lenA:
      if arr[j]-arr[i]==d:
        count+=1
        i=j
        break
      else:
        j+=1
    if count==3:
      rCount+=1
      count=1
      sPtr+=1
      i=sPtr
    if j >=lenA -1:
      count=1
      sPtr+=1
      i=sPtr
  return rCount

print(beautifulTriplets(3,[1, 2, 4, 5, 7, 8, 10]))





