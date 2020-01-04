import math
def encryption(s):
  result=''
  l=len(s)
  srt=math.sqrt(l)
  ll=math.floor(srt)
  ul=0
  if ll<srt:
    ul=ll+1
  else:
    ul=ll
  if ll*ul < l:
    ll+=1
  p=0
  j=ul-p
  print(l,ll,ul,p,j)
  while p<ul:
    i=p
    while i<l:
      result+=s[i]
      i+=j
    result+=' '
    p+=1
  return result

print(encryption('wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny'))
    
