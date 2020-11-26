password = "abc123"
passwordCheck = str(input("Please enter your password: "))

while password != passwordCheck:
  if passwordCheck == "help":
    print("The first letter of the password is 'a'.")
    break
  else:
    print("Wrong password")
    break

if password == passwordCheck:
  print("Welcome!")