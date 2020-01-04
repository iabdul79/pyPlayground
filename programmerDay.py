def dayOfProgrammer(year):
  svnMnths = 215
  feb = 0
  if year > 1918:
    feb = 28 if year % 4 else 29
  elif year < 1918:
    feb = 29 if (not year%400 or (not (year % 4) and year % 100)) else 28
  else:
    feb = 15
  return str(256 - (feb + svnMnths)) + '.09.' + str(year)

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year