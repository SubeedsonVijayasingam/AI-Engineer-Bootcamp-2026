#challenge6 -Find the highest mark

marks ={
    "math": 85,
    "science": 90,
    "english": 78,
    "computer": 95
}
highest_sub = max(marks, key=marks.get)
highest_mark = marks[highest_sub]

print("Highest subject:", highest_sub)
print("Highest mark:", highest_mark)