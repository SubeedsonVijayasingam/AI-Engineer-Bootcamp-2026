#challenge5 - login system

username = input("Enter username: ")
password = input("Enter password: ")

if username != "admin":
    print("Incorrect username")
elif password != "python123":
    print("Incorrect password")
else:
    print("Login Successful")