gpa  = float(input("Please input your GPA:"))
number_of_lectures  = float(input("Please input the number of lectures you had:"))

if gpa < 2.0:
  if number_of_lectures < 47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if number_of_lectures < 47:
    print("Not enough numbers of lectures!")
  else:
    print("GRADUATED!")