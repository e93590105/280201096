parameter_a = float(input("Please input the first parameter:"))
parameter_b = float(input("Please input the first parameter:"))
parameter_c = float(input("Please input the first parameter:"))

delta = float(parameter_b**2 - 4*parameter_a*parameter_c)
i = -1**0.5
if delta == 0 :
  root_1 = (-1*parameter_b)/(2*parameter_a)
  print("The root of the equation is" , root_1)
elif delta > 0:
  root_2 = (-parameter_b+delta**0.5)/2*parameter_a
  root_3 = (-parameter_b-delta**0.5)/2*parameter_a
  print("The roots of the equation are" , root_2 , " and " , root_3)
else:
  root_4 = (-parameter_b+delta**0.5)/2*parameter_a
  root_5 = (-parameter_b-delta**0.5)/2*parameter_a
  print("The roots of the equation are" , root_4 , " and ", root_5)