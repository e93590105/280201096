email = str(input("Please enter the email adress you want to be checked:"))
reference = "ceng113@example.com"

if "@" in email:
  email = email.lower()
  part1 = email.split("@")[0]
  part1 = part1.replace(".","")
  part2 = email.split("@")[1]
  email = part1 + "@" + part2

  print(email)

  if email == reference:
    print("Equal")
  else:
    print("Not equal")
else:
  print("Not equal")