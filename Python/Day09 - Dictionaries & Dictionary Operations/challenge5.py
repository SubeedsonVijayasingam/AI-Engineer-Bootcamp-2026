#challenge5 - Dictionary Analyzer

marks = {
    "math": 85,
    "science": 90,
    "english": 78
}
print(f"Subjects: {marks.keys()}")
print(f"Marks: {marks.values()}")
print(f"Number of subjects: {len(marks)}")
print(f"Total marks: {sum(marks.values())}")