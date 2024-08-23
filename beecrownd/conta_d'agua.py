m = int(input(''))

if m <= 10:
  print('7')
elif m >= 11 and m <= 30:
  print(7 + (m - 10) * 1)
elif m >= 31 and m <= 100:
  print(7 + 20 + (m - 30) * 2)
else:
  print(7 + 20 + 140 + (m - 100) * 5)