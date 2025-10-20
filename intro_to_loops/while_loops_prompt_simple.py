# Prompt the user to enter a response, and loop until the user wants to quit
quit = False
user = "no" # default

while user.lower() != "yes":
    user = input("Do you want to quit? (yes/no): ")

print("The user quit")