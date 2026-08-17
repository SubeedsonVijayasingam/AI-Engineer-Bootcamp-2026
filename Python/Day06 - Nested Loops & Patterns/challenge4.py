#challenge4 - Number triangle

n=int(input("Enter a size: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()