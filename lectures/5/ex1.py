numberList = []
n  = int(input("How many number do you have?"))
for i in range(n):
  i = int(input("Please enter an integer:"))
  numberList.append(i)
sortedNumber = sorted(numberList)
squares = []
for i in sortedNumber:
  x = i*i
  squares.append(x)
print(squares)