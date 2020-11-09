number = int(input("Please input the number :"))
if number in range(0,10):
  total = number
else:
  ones = number % 10
  tens = (number//10) % 10
  total = ones + tens
print("Sum of last two digits: " , total)