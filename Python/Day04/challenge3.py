#challenge3

n = int(input("Enter a number: "))

if n<0:
    print("Negative")
elif n==0:
    print("Zero")
else:
    print("Positive")

if n%2==0:
    print("Even")
else:
    print("Odd")

if n>100:
    print("Greater than 100: True")
else:
    print("Greater than 100: False")