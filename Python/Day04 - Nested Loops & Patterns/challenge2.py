#challenge2 - eligibility checker

age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))

if age >=18 and cgpa >= 7.0:
    print("Eligible: True")
else:
    print("Eligible: False")