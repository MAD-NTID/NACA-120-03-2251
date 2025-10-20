# Prompt the user to enter a response, and loop until the user wants to quit
quit = False

while quit == False:
    # Prompt the user if he/she wants to quit
    user = input("Do you want to quit? (yes/no): ")
    # if user.lower() == "yes":
    #     quit = True
    quit = user.lower() == "yes"

print("The user quit")