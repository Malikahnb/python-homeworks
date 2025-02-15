name = input('Enter a username: ')
psswd = input('Enter a password: ')

if bool(name.strip()) and bool(psswd.strip()):
    print("Username and password are valid.")
else:
    print("Username or password cannot be empty.")