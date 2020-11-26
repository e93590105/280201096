num1 = str(input("Please enter the first positive integer:"))
num2 = str(input("Please enter the second positive integer:"))

number1 = []
number2 = []
for i in num1:
  number1.insert(0,i)
for i in num2:
  number2.insert(0,i)

numberRange = 0

if len(number1) > len(number2):
  numberRange = len(number2)
else:
  numberRange = len(number1)

matches = 0

for i in range(0,numberRange):
  if number1[i] == number2[i]:
    matches = matches+1
print(matches)