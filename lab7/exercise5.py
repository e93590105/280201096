password = input("Please enter a password: ")
checker = list(password)
uppercase = []
lowercase = []
number = []
for chr in password:
  if chr.isnumeric() == True:
    number.append(chr)
  elif chr.isupper() == True:
    uppercase.append(chr)
  elif chr.islower() == True:
    lowercase.append(chr)
if len(uppercase) ==0 or len(lowercase)==0 or len(number)==0:
  print("Not valid")
elif len(checker)<8:
  print("Not valid")
else:
  print("Valid")