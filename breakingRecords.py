def breakingRecords(scores):
  if not scores:
    return [0, 0]
  minCount=0
  maxCount=0
  minNo = scores[0]
  maxNo = scores[0]
  for score in scores:
    if score > maxNo :
      maxNo = score
      maxCount+=1
    if score < minNo :
      minNo = score
      minCount+=1
  return [maxCount, minCount]

print(breakingRecords([17, 45, 41, 60, 17, 41, 76, 43, 51, 40, 89, 92, 34, 6, 64, 7, 37, 81, 32, 50]))
