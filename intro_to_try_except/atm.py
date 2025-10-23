# ATM - allows to withdraw or deposit cash | mula | money
starting_money = 500

print("Customer Inserts Card...")
print("Card Read...")

# string
pin = input("Enter your pin number: ")

if pin == "1234":
    print("Welcome to your Bank Account - whatcha wanna do: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Cancel")
    option = input("Select an Action: ")

    if option == "withdraw" or option == "1":
        try:
            amount = int(input("How much do you wanna withdraw? "))
            starting_money -= amount
        except TypeError as te:
            print("Hold up pal. Something is not right. That ain't money")
            print(te)
        except ValueError as ve:
            print("Ah come on, that's not money")
            print(ve)
        # safety net
        except:
            print("Something went wrong")

    elif option == "Deposit":
        pass

    elif option == "Cancel":
        pass
    
    else:
        print("Invalid")
else:
    print("Invalid input. Sorry Pal")