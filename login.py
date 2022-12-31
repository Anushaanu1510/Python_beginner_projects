import time

username = "Anusha"
password = "secretpassword"

username_input = input("Username:")
password_input = input("Password:")

if username_input == username and password_input == password:
    print("Acces Granted")
    print("Please Wait")
    time.sleep(5)
    print("ok...Loading...")
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print("You have a security clearence")
    print(username, "Welcome to the world of python")
elif username_input != username and password_input == password:
    print("Username is incorrect")
elif username_input == username and password_input != password:
    print("Password is incorrect")
else:
    print("You have entered wrong username and password")
