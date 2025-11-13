import random as rand

# Create the empty queue list
queue = []

def size():
    return len(queue)

def empty():
    return size() == 0

def enqueue(element):
    queue.append(element)

def peek():
    if not empty():
        return queue[0]
    
    return None

def dequeue():
    return queue.pop(0)

# Application Functions
def add_print_job(job):
    random_print_job_id = str(rand.randrange(0, 9999))
    enqueue(f"{job} - Print Job {random_print_job_id}")

def print_a_job():
    print_job = dequeue()
    return print_job

def print_job_name_prompt():
    while True:
        print_job = input("Enter a name for the print job: ")

        if print_job is not None and len(print_job) > 0:
            return print_job

def main():
    print("Welcome to My Print Station\n")

    while True:
        choice = input("Enter an option - \n" \
                       "1. Add a Print Job\n" \
                       "2. Print\n" \
                       "3. Show All Print Jobs\n" \
                       "4. Print All Jobs \n" \
                       "5. Clear All Prints \n" \
                       "6. Exit\n\n"                       
                       "Enter Choice (1-6): "
                       )
        
        if choice == "1":
            print_job = print_job_name_prompt()

            add_print_job(print_job)
            print(f"Print job '{print_job}' added successfully")

        elif choice == "2":
            print(f"Printed: '{print_a_job()}'")

        elif choice == "3":
            print(f"All ({size()}) Print Jobs Available: ")
            for print_job in range(size()):
                print(f"{queue[print_job]}")

        elif choice == "4":
            # for print_job in range(size()):
            while not empty():
                print(f"Printed: '{print_a_job()}'")

        elif choice == "5":
            queue.clear()
            print("All print jobs deleted")

        elif choice == "6":
            print("Thank you for using my printing machine")
            break

        else:
            print("Invalid Menu Choice")

        print()
main()