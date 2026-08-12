#challenge4

n = int(input("Enter a number: "))

count = 0

for i in range(1, n+1):
    if i%2 == 0:
        count += 1
print(f"Even numbers count: {count}")