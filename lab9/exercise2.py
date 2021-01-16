def reverseList(x):
  reversed_list = []
  if len(x) == 1:
    reversed_list.insert(0,x[0])
  else:
    reversed_list.insert(0,x[-1])
    reverseList(x[0:len(x)-2])
list1 = [1, 2, 3, 4]
print(reverseList(list1))