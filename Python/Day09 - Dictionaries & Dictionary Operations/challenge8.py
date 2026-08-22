# challenge8 - Search for a Subject

marks = {
    "math": 85,
    "science": 42,
    "english": 78,
    "computer": 35,
    "history": 67
}

subject = input("Enter subject: ")

if subject in marks:
    print(f"Mark: {marks[subject]}")
else:
    print("Subject not found")