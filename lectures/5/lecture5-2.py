number = int(input("Please enter a number:"))
triangularValue = 0
for value in range(number+1):
  triangularValue = triangularValue + value
print("Triangular value of ", number , " is ", triangularValue , ".")