answer = True
x = int(input("Please enter an integer:"))
for count in range(2,x-1):
  remainder = x%count
  if remainder == 0:
    answer = False
print(answer)