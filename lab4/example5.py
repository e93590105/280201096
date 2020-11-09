n = int(input("Please enter the number that you want its factorial to be calculated: "))
factorial = 1
for i in range(1, n+1):
  factorial *= i 
print(factorial)