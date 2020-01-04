def getMoneySpent(keyboards, drives, b):
  mp = 0
  for k in keyboards:
    for d in drives:
      if k+d > mp and k+d <=b:
        mp = k+d
  return mp if mp > 0 else -1

print(getMoneySpent([3, 1],[5, 2, 8], 10))