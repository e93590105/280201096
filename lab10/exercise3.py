def sumOfList(x):
  if not isinstance(x, list):
    return x
  else:
    sum = 0
    for a in x:
      sum += sumOfList(a)
    return sum

a_list = [3,12,76,[4,56,43],[2,8],81,75]

print(sumOfList(a_list))