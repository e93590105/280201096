n = int(input("How many integers do you have?"))
sum = 0
for i in range(n):
  x = int(input("Enter an integer:"))
  sum = sum + x
print("The average is " , sum/n)