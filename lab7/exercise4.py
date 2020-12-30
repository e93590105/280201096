employees = {}
for i in range(5):
  empName = input("Please enter the name of the employee:")
  empSalary = input("Please enter the salary of the employee:")
  employees[empName] = empSalary
maxs = sorted(employees.values())
print(maxs)