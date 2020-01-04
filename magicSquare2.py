def formingMagicSquare(s):
  w=0
  w+=correctFive(s)
  w+=correctMiddle(s)
  w+=correctCornors(s)
  return s

def remaining(s):
  w=0
  _i=0
  while _i < len(s):
    _j = 0
    if _i == 1 and _j == 1:
      w+=correctFive(s[_i][_j])
    elif _i == 1 or _j == 1:

    else:
      w+=correctCornors(s,_i,_j)

def correctFive(e):
  if e != 5:
    return abs(e - 5)
  return 0

def correctCornors(s, i, j):
  _s = [2,8,6,4]
  if i == 0 || j == 0:
    s[]