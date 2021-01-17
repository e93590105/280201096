def reverseList(x):
  reversed_list = []
  if len(x) == 0:
    return []
  else:
    return [x[-1]]+reverseList(x[:-1])
list1 = [1, 2, 3, 4]
print(reverseList(list1))