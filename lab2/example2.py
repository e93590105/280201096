number1 = float(input("Please input the first number:"))
number2 = float(input("Please input the second number:"))
number3 = float(input("Please input the third number:"))

if number1 < number2:
  if number1 < number3:
    print("The number which has the minimum value above these three numbers is" , number1)
  else:
      print("The number which has the minimum value above these three numbers is" , number3)
else:
  if number1 < number3:
    print("The number which has the minimum value above these three numbers is" , number2)
  else:
      print("The number which has the minimum value above these three numbers is" , number3)


