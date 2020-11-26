numberOfNumbers = int(input("Please enter how many numbers you'd like to include to the calculation:"))
numbers = []
evenNumbers = []
for i in range(0,numberOfNumbers):
  numbers.append(int(input("Enter an integer:")))
for i in numbers:
  if i%2 == 0:
    evenNumbers.append(i)
  
percentNum = len(evenNumbers)/len(numbers)*100
print("Ratio of even numbers to the all numbers is: %" , percentNum)
