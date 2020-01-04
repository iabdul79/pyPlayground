def matchingStrings(st, qu):
  qlen = len(qu)
  slen=len(st)
  res=[0]*qlen
  i=0
  while i<qlen:
    for j in st:
      if j == qu[i]:
        res[i]+=1
    i+=1
  return res

print(matchingStrings([
'abcde',
'sdaklfj',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf',
'na',
'asdjf',
'na',
'basdn',
'sdaklfj',
'asdjf',
],
[
'abcde',
'sdaklfj',
'asdjf',
'na',
'basdn',
]))
