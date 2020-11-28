number = int(input("Please enter the number of items in your list: "))

primaryList = []
for i in range(number):
  element = int(input("Please enter an integer: "))
  primaryList.append(element)

for x in primaryList:
  while primaryList.count(x) > 1:
    primaryList.remove(x)

numberList = list(reversed(sorted(primaryList)))
print(numberList)