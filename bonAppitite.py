def bonAppetit(bill, k, b):
  toPay = 0
  for item in range(len(bill)):
    if item == k:
      continue
    toPay+=bill[item]/2
    
  print('Bon Appetit') if toPay == b else print(int(b-toPay))

print(bonAppetit([3, 10, 2, 9], 1, 7))