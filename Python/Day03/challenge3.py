#challenge3

mark = int(input("Enter your mark: "))

if 90 <= mark<=100:
    print("A")
elif 80 <= mark<=89:
    print("B")
elif 70 <= mark<=79:
    print("C")
elif 60 <= mark<=69:
    print("D")
elif 0 <= mark <= 59:
    print("F")
else:
    print("Invalid mark")