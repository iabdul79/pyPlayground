def truckTour(petrolpumps):
  p=petrolpumps
  plen=len(p)
  inTank=0
  c=0
  count=0
  i=c
  while count<plen:
    if i==plen:
      i=0
    inTank+=p[i][0]-p[i][1]
    if inTank>0:
      count+=1
    else:
      count=0
      c=i+1
      inTank=0
      if c>=plen:
        c=-1
        break
    i+=1
  return c

print(truckTour([
[5 ,1],
[6, 10],
[4 ,3],
[2,4],
[4,2],
[2,6]
]))

