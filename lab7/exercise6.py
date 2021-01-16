numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
set1 = set(numbers1)
set2 = set(numbers2)
intersection = []
for i in set1:
  if i in set2:
    intersection.append(i)
print(intersection)
union = []
for element in set1:
  union.append(element)
for element in set2:
  if element not in intersection:
    union.append(element)
print(union)