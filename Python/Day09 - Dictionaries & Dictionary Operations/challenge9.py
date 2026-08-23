# challenge9 - Count Subjects Above a Mark

marks = {
    "math": 85,
    "science": 42,
    "english": 78,
    "computer": 35,
    "history": 67
}

minimum = int(input("Enter minimum mark: "))

count = 0

for mark in marks.values():
    if mark >= minimum:
        count += 1

print(f"Subjects above {minimum}: {count}")