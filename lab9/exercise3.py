def get_evens(x):
  count = 0
  if x == []:
    return count
  else:
    if x[0] % 2 == 0:
      count +=1
      return get_evens(x[1:])
    else:
      return get_evens(x[1:])


a = [1,2,3,4,5,6]
print(get_evens(a))
