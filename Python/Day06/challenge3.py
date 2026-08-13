#challenge3 - decreasing star triangle

n = int(input("Enter a size: "))

for i in range(1, n+1):
    for j in range(n-i+1):
        print("*", end=" ")
    print()