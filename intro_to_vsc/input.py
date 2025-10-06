# The correct password the user must enter
# Shhh... don't tell the user.
CURRENT_PASSWORD = "topS3cret"

# Print and Read using standard input()
# hello world this a comment
"""
hello world
this is a multi line
comment
i can type as long as 
i want...
"""
input_password = input("Enter the password: ")

if input_password == CURRENT_PASSWORD:
    print("Welcome Admin")
else:
    print("Incorrect username and password")