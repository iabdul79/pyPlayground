def queensAttack(n, k, r_q, c_q, obstacles):
  qp=[r_q,c_q]
  da=[0]*8
  da[0]=min(n-r_q, c_q-1)
  da[1]=n-r_q
  da[2]=min(n-r_q, n-c_q)
  da[3]=n-c_q
  da[4]=min(n-c_q,r_q-1)
  da[5]=r_q-1
  da[6]=min(r_q-1,c_q-1)
  da[7]=c_q-1
  totl=0
  for p in obstacles:
    if p[0]>qp[0] and p[1]<qp[1]:
      if abs(p[0]-qp[0]) == abs(p[1]-qp[1]):
        da[0]=min(da[0],qp[1]-p[1]-1)
    elif p[0]>qp[0] and p[1]==qp[1]:
      da[1]=min(da[1],p[0]-qp[0]-1)
    elif p[0]>qp[0] and p[1]>qp[1]:
      if abs(p[0]-qp[0]) == abs(p[1]-qp[1]):
        da[2]=min(da[2],p[1]-qp[1]-1)
    elif p[0]==qp[0] and p[1]>qp[1]:
      da[3]=min(da[3],p[1]-qp[1]-1)
    elif p[0]<qp[0] and p[1]>qp[1]:
      if abs(p[0]-qp[0]) == abs(p[1]-qp[1]):
        da[4]=min(da[4],p[1]-qp[1]-1)
    elif p[0]<qp[0] and p[1]==qp[1]:
      da[5]=min(da[5],qp[0]-p[0]-1)
    elif p[0]<qp[0] and p[1]<qp[1]:
      if abs(p[0]-qp[0]) == abs(p[1]-qp[1]):
        da[6]=min(da[6],qp[0]-p[0]-1)
    elif p[0]==qp[0] and p[1]<qp[1]:
      da[7]=min(da[7],qp[1]-p[1]-1)
  for d in da:
    totl+=d
  return totl