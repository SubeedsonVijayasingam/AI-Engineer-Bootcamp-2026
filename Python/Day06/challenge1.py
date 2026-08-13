#challenge1 - print a square

n =int(input("Enter a size: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()