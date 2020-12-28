def hailstone(x):
  s = str(x)
  if x == 1:
    return s
  else:
    if x%2 == 0:
      return s + "," + hailstone(x//2)
    else:
      return s + "," + hailstone(3*x+1)
