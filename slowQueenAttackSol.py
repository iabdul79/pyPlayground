def queensAttack(n, k, r_q, c_q, obstacles):
  #oa=classifyObstacles([r_q, c_q], obstacles)
  tMoves=0
  tMoves+=ulMove(n, [r_q,c_q], obstacles)
  tMoves+=uMove(n, [r_q,c_q], obstacles)
  tMoves+=urMove(n, [r_q,c_q], obstacles)
  tMoves+=rMove(n, [r_q,c_q], obstacles)
  tMoves+=lrMove(n, [r_q,c_q], obstacles)
  tMoves+=dMove(n, [r_q,c_q], obstacles)
  tMoves+=llMove(n, [r_q,c_q], obstacles)
  tMoves+=lMove(n, [r_q,c_q], obstacles)
  return tMoves

def ulMove(n, qp, obs):
  mv=0
  i=qp[0]+1
  j=qp[1]-1
  while i<=n and j>0:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i+=1
    j-=1
  return mv

def uMove(n, qp, obs):
  mv=0
  i=qp[0]+1
  j=qp[1]
  while i<=n:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i+=1
  return mv

def urMove(n, qp, obs):
  mv=0
  i=qp[0]+1
  j=qp[1]+1
  while i<=n and j<=n:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i+=1
    j+=1
  return mv

def rMove(n, qp, obs):
  mv=0
  i=qp[0]
  j=qp[1]+1
  while j<=n:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    j+=1
  return mv

def lrMove(n, qp, obs):
  mv=0
  i=qp[0]-1
  j=qp[1]+1
  while i>0 and j<=n:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i-=1
    j+=1
  return mv

def dMove(n, qp, obs):
  mv=0
  i=qp[0]-1
  j=qp[1]
  while i>0:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i-=1
  return mv

def llMove(n, qp, obs):
  mv=0
  i=qp[0]-1
  j=qp[1]-1
  while i>0 and j>0:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    i-=1
    j-=1
  return mv

def lMove(n, qp, obs):
  mv=0
  i=qp[0]
  j=qp[1]-1
  while j>0:
    if findOb(i,j, obs):
      return mv
    else:
      mv+=1
    j-=1
  return mv

def findOb(r,c,obs):
  for o in obs:
    if o[0] == r and o[1] == c:
      return 1
  return 0

print(queensAttack(5,3,4,3,[[5, 5],[4, 2],[2, 3]]))