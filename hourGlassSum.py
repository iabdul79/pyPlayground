def hourglassSum(arr):
  maxSum=-63
  rlen=len(arr)
  clen=len(arr[0])
  i=0
  while i<rlen-2:
    j=0
    while j<clen-2:
      sumX=hrSum(arr, i, j)
      maxSum = max(sumX, maxSum)
      j+=1
    i+=1
  return maxSum

def hrSum(arr, i, j):
  return arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

print(hourglassSum([
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0],
]))

