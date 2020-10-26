age = float(input("Please input your age:"))
normal_price = 3
if 6 < age < 60:
  if 6 < age < 18:
      print("You will pay" , normal_price/2 , "TLs.")
  else:
      print("You will pay" , normal_price , "TLs.")
else:
    print("You will pay" , 0 , "TLs.")
