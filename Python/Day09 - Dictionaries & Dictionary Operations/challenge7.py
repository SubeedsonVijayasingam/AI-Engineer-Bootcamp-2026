#challenge7 - count pass and fail

marks = {
    "math": 85,
    "science": 42,
    "english": 78,
    "computer": 35,
    "history": 67
}

pass_count = 0
fail_count = 0

for mark in marks.values():
    if mark >=40:
        pass_count +=1
    else:
        fail_count +=1
print(f"Pass count: {pass_count}")
print(f"Fail count: {fail_count}")