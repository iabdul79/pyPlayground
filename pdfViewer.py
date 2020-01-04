def designerPdfViewer(h, word):
  ml=0
  le=0
  for w in word:
    k=h[ord(w)-ord('a')]
    if k > ml:
      ml=k
    le+=1
  return le*ml

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba'))