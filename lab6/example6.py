n = input("Please enter a number: ")
matrix = []
for i in range(int(n)**2):
  element = input("Please enter an integer: ")
  matrix.append(int(element))
print(matrix)

trace = 0
count = 0
while count<int(n):
  trace = trace+matrix[count*int(n)+count]
  count += 1
  
print(trace)