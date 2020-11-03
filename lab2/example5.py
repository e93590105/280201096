month = input("Input the month e.g. 'January','March','December' etc. : ")
day = int(input("Input the day: "))

if month in ("January", "February", "March"):
  season = "Winter"
elif month in ("April", "May", "June"):
  season = "Spring"
elif month in ("July", "August", "September"):
  season = "Summer"
else:
  season = "Autumn"

  if (month == "March") and (day > 19):
    season = "Spring"
  elif (month == "June") and (day > 20):
    season = "Summer"
  elif (month == "September") and (day > 21):
    season = "Autumn"

  elif (month == "December") and (day > 20):
    season = "Winter"

print("Season is", season)