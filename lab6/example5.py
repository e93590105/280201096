number = int(input("Please enter a number: "))
matrix = []
count = 0
for i in range(number):
  temp = []
  for x in range(number-1):
    temp.append(0)
  temp.insert(i,1)
  matrix.append(temp)
string = ""
for element in matrix:
  stringtemp = ""
  for elm in element:
    stringtemp = stringtemp + str(elm) +" "
  string = string + stringtemp + "\n"
print(string)