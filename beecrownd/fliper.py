num1, num2 = input().split()

num1= int(num1)
num2 = int(num2)

if num1 == 1 and num2 == 0:
  print('B')
elif num1 == 0 and num2 == 0:
  print('C')
elif num1 == 0 and num2 == 1:
  print('C')
elif num1 == 1 and num2 == 1:
  print('A')