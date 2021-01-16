def harmonicSum(n):
  sum = 0
  if n == 1:
    sum = sum +1
  else:
    sum = sum+1/n+harmonicSum(n-1)
  return sum
print(harmonicSum(5))