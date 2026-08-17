#challenge4 - login system

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
elif username != "admin" and password == "python123":
    print("Incorrect username")
elif password != "python123" and username == "admin":
    print("Incorrect password")
else:
    print("Login Failed")