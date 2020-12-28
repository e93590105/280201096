def PascalsTriangleLastLine(n):
  if n == 1:
    return [1]
  else:
    line = [1]
    previousLine = PascalsTriangleLastLine(n-1)
    for i in range(len(previousLine)-1):
      line.append(previousLine[i]+previousLine[i+1])
    line += [1]
    return line

print(PascalsTriangleLastLine(6))