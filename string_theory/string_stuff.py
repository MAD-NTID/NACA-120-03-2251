def prompt_user_for_make():
    makes = ["toyota", "subaru", "honda", "suzuki", "kia", 
             "hyundai", "mitsubishi", "chrysler", "chevrolet"]
    
    # user join to provide options
    user_input = input(f"Select a make from the following ({", ".join(makes)}):")

    # make it lower 
    user_input.lower()

    # validate it's in the list
    if user_input in makes:
        print(f"That's a good choice, you picked {user_input}")
    else:
        print("Not a valid make of car")

def list_makes_in_reverse_order():
    makes = ["toyota", "subaru", "honda", "suzuki", "kia", 
             "hyundai", "mitsubishi", "chrysler", "chevrolet"]
    
    print(f"Original Order: {", ".join(makes)}")

    reversed_makes = makes[::-1]

    print(f"Reversed Order: {", ".join(reversed_makes)}")

def replace_strings():
    while True:
        # ask the user to enter a random string
        random = input("Enter a random sentence: ")

        # ask the user to enter a string to replace
        word_to_replace = input("Enter a string to replace: ")

        # ask the user to enter the replacement string
        string_to_replace = input("Enter the replacement string: ")

        print()
        print("Before Replacement")
        print(random)
        print(f"After Replacing '{word_to_replace}' with '{string_to_replace}'")
        
        replacement = random.replace(word_to_replace, string_to_replace)
        print(replacement)

prompt_user_for_make()
list_makes_in_reverse_order()
replace_strings()
