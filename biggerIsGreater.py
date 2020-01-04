def biggerIsGreater(w):
  lenS = len(w)
  i=lenS-1
  while i>0:
    j=i-1
    if ord(w[i]) > ord(w[j]):
      l=i
      while i<lenS:
        if ord(w[i]) <= ord(w[j]):
          break
        i+=1
        l=i-1
      return w[0:j]+w[l]+''.join(sorted(w[l+1:lenS]+w[j:l]))
    i-=1
  return 'no answer'

print(biggerIsGreater('vvvygfabrsqeitgelpxwodhdfyypoyufxnecmrtkbzbhzfbtvnffcmikqoosfzoozssonomkgmtdqfecrqtps'))