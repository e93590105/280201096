def PascalsTriangle(n):
  if n == 1:
    return [[1]]
  else:
    line = [1]
    allLines = PascalsTriangle(n-1)
    lastLine = allLines[-1]
    for i in range(len(lastLine)-1):
      line.append(lastLine[i]+lastLine[i+1])
    line += [1]
    allLines.append(line)
    return allLines

print(PascalsTriangle(4))