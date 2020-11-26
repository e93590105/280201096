gradeList = []
numberOfStudents = int(input("Please enter the number of students:"))
for i in range(numberOfStudents):
  print("Student " , str(i+1))
  mid1 = int(input("Midterm 1: "))
  mid2 = int(input("Midterm 2: "))
  final = int(input("Final: "))
  gradeList.append([mid1,mid2,final])
print(gradeList)

averageGrades = []
for sub_grades in gradeList:
  averageGrades.append(sub_grades[0]*0,3 + sub_grades[1]*0,3 + sub_grades[2]*0,4)
print(averageGrades)