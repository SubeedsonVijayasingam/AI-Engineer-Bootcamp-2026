#challenge5

name = input("Name: ")
age = int(input("Age: "))
cgpa = float(input("CGPA: "))
projects = int(input("Projects: "))

print("==== STUDENT PERFORMANCE ====")
print(f"Name: {name}")
if age >= 18:
    print("Age Status: Adult")
else: 
    print("Age Status: Minor")

if cgpa >= 8.0:
    print("CGPA Status: Excellent")
elif cgpa >=7.0:
    print("CGPA Status: Good")
elif cgpa >=6.0:
    print("CGPA Status: Average")
else:
    print("CGPA Status: Needs Improvement")

if projects >=3:
    print("Project Status: Good project experience")
else:
    print("Project Status: Needs more project")


if age>=18 and cgpa>=7.0 and projects>=2:
    print("Eligible: True")
else:
    print("Eligible: False")