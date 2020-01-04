def divisibleSumPairs(n, k, ar):
  pair = 0
  i = 0
  while i < n:
    j = i + 1
    while j < n:
      pair = pair + 1 if (ar[i] + ar[j]) % k == 0 else pair
      j=j+1
    i=i+1
  return pair


def divisibleSumPairs(n, k, ar):
  nums = [0] * k
  count = 0
  for ele in ar:
      modu = ele % k
      count += nums[(k - modu) % k]
      nums[modu] += 1
  return count

print(divisibleSumPairs(7, 3, [1, 3, 2, 6, 4, 5, 9]))
