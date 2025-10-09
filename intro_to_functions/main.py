def check_password(password):
    if password == "admin":
        return True
    else:
        return False

def check_username(username):
    if username == "tony" or username == "Tony":
        return True
    else:
        return False

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if check_username(username) and check_password(password):
        print("Welcome home, Tony Stark")
    else:
        print("Sorry, you ain't no Tony Stark")

main()