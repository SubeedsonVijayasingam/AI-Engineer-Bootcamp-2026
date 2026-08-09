#challenge2

name = input("Enter your name: ")
age =int(input("Enter your age: "))
department = input("Enter your department: ")
cgpa = float(input("Enter your cgpa: "))
projects = int(input("Enter your number of projects: "))
adding_project = projects + 1

print(f" ==== STUDENT DETAILS ====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Department: {department}")
print(f"CGPA: {cgpa}")
print(f"Projects: {projects}")
print(f"Projects after next project: {adding_project}")

print(f" ==== DATA TYPES ====")
print(f"Name: {type(name)}")
print(f"Age: {type(age)}")
print(f"Department: {type(department)}")
print(f"CGPA: {type(cgpa)}")
print(f"Projects: {type(projects)}")