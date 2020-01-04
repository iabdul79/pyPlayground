def repeatedString(s, n):
  slen=len(s)
  rept=int(n/slen)
  bal=n%slen
  aCount=rept*getCountinS('a',s)
  if bal > 0:
    aCount+=getCountinS('a',s[0:bal])
  return aCount

def getCountinS(c, strn):
  ccount=0
  for i in strn:
    if i == c:
      ccount+=1
  return ccount

print(repeatedString('a',1000000000000))
