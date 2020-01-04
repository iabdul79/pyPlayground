def climbingLeaderboard(scores, alice):
  ranks = createRanksArray(scores)
  print('ranks', ranks)
  print('alice', alice)
  ar = []
  _i=0
  while _i < len(alice):
    i=0
    j=len(ranks)-1
    _r = aliceRank(ranks, alice[_i], i, j)
    ar.append(_r)
    _i+=1
  return ar

def createRanksArray(s):
  r=1
  ra=[s[0]]
  i=1
  while i<len(s):
    if s[i] < s[i-1]:
      r+=1
      ra.append(s[i])
    i+=1
  return ra

def aliceRank(r, a, i, j):
  mid = i + int((j-i)/2)
  if a == r[mid]:
    return mid+1
  if i >= j:
    if r[i] < a:
      return i+1
    else:
      return i+2
  if a > r[mid]:
    return aliceRank(r, a, i, mid-1)
  elif a < r[mid]:
    return aliceRank(r, a, mid+1, j)

print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))

