number = int(input("Please enter how many Fibonacci numbers you want to generate:"))

fibonacci = [0,1]

for i in range(number+1):
  x = fibonacci[i]+fibonacci[i+1]
  fibonacci.append(x)
print(fibonacci[1:number+1])