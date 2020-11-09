firstNumber = int(input("Please enter the first number: "))
secondNumber = int(input("Please enter the second number: "))
power = 1
if secondNumber < 0:
  print("Please make sure that your second number is greater than or equals to 0.")
else:
  for i in range(secondNumber):
    power *= firstNumber
  print(power)
