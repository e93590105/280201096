n = int(input("How many numbers are there?"))
maxNum = int(input("Please enter a number:"))
for i in range(n-1):
  x = int(input("Enter a number:"))
  if x > maxNum:
    maxNum = x
print("The largest value is " , maxNum)