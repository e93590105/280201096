def PascalsTriangle(n):
  if n == 1:
    return [[1]]
  else:
    triangle = [[1]]
    line = [1]
    
    previousLine = PascalsTriangle(n-1)
    for i in range(len(previousLine)-1):
      line.append(previousLine[i]+previousLine[i+1])
      triangle.append(line) 
      
    line += [1]
    
    return line

print(PascalsTriangle(4))