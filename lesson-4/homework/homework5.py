passw = input("Enter the password: ")

if len(passw) < 8:
    print('Password is too short!')
    for i in passw:
        if i.isupper():
            print("Password is strong")
        else:
            print('Password must contain an uppercase letter.')



