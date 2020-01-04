def countingValleys(n, s):
  stepCount=0
  vallyCount=0
  for _s in s:
    atSea = 1 if stepCount == 0 else 0
    if _s == 'U':
      stepCount = stepCount +1
    else :
      stepCount = stepCount -1
    if atSea and stepCount < 0:
      vallyCount+=1
  return vallyCount
    

print(countingValleys(12, 'DDUUDDUDUUUD'))