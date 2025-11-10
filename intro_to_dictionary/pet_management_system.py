import random as rand

"""
You are tasked with creating a simple system to record information about pets
For each pet, you need to have the following:
Type – cat, dog, bird, turtle, etc.
Name – the pet’s name (“Spike”, “Fluffy”, etc.).
Age – the pet’s age as a number (2.0, 3.5, 7.0, etc.).
“Patient Number” – unique # identifying each pet.
How would you structure the dictionary?
"""
veterinarian_pet_dictionary = {}

def add_pet(patient_number, type, name, age):
    veterinarian_pet_dictionary[patient_number] = (type, name, age)
    print(f"Pet Added: {patient_number} - {", ".join(veterinarian_pet_dictionary[patient_number])}")

def generate_patient_number():
    while True:
        patient_number = str(rand.randint(1, 100000))

        # Validate Patient Number is Unique
        if patient_number in veterinarian_pet_dictionary:
            print("Duplicate Patient Number - Regenerating")
        else:
            return patient_number

def prompt_type():
    allowed_types = ["dog", "cat", "bird", "reptile", "aquatic", "others"]

    while True:
        pet_type = input(f"Enter the pet's type - (Pet Types: {str(", ".join(allowed_types))}): ").lower()

        if pet_type in allowed_types:
            return pet_type
        else:
            print("Invalid pet type\n")

def prompt_name():
    while True:
        pet_name = input("Enter the pet's name: ")

        # Can't be empty or None
        if pet_name is not None and pet_name != "":
            return pet_name
        else:
            print("Invalid Pet Name\n")

def prompt_age():
    while True:
        try:
            age = float(input("Enter the pet's age: "))

            # Age can't be negative
            if age >= 0:
                return str(age)
            else:
                print("Age can't be negative")
        except:
            print("Invalid Age\n")

def show_pets():
    # This just prints the whole dictionary and everything in it
    # print(veterinarian_pet_dictionary)

    # This displays only the patient number for each pet (much cleaner)
    listing = 1
    for key in veterinarian_pet_dictionary:
        print(f"{listing}) - Patient ID: {key}")

def main():
    print("Welcome to AXSA's Veterinary Hospital\n")

    while True:
        choice = input("Select from the options below -\n"\
            "1) Add a Pet \n" \
            "2) Remove Pet\n" \
            "3) Display Record\n" \
            "4) Exit\n\n" \
            "Select: ")
        
        if choice == "1":
            patient_number = generate_patient_number()
            pet_type = prompt_type()
            pet_name = prompt_name()
            pet_age = prompt_age()

            add_pet(patient_number, pet_type, pet_name, pet_age)

        elif choice == "2":
            show_pets()

            patient_number_to_display = input("Enter the patient number of the pet to remove: ")

            if patient_number_to_display in veterinarian_pet_dictionary:
                pet_found = veterinarian_pet_dictionary.pop(patient_number_to_display)

                print(f"Removed Pet: {pet_found}")
            else:
                print(f"Pet patient number '{patient_number_to_display}' not found")

        elif choice == "3":
            show_pets()

            patient_number_to_display = input("Enter the patient number of the pet to remove: ")

            if patient_number_to_display in veterinarian_pet_dictionary:
                pet_found = veterinarian_pet_dictionary[patient_number_to_display]

                print(f"Pet Records: {pet_found}")
            else:
                print(f"Pet patient number '{patient_number_to_display}' not found")

        elif(choice == "4"):
            break
        else:
            print("Invalid Choice")

        print()

    print("Thank you for using AXSA's Pet Management System. Good Bye. All data is now lost")

# DO NOT FORGET TO INVOKE THE MAIN FUNCTION
main()