def check_password(password):
    return password == "admin"

def check_username(username):
    return username == "tony" or username == "Tony"

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if check_username(username) and check_password(password):
        print("Welcome home, Tony Stark")
    else:
        print("Sorry, you ain't no Tony Stark")

main()