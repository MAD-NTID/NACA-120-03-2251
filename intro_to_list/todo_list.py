# CREATE A TO DO LIST 
# THE APP ALLOWS TO ADD, REMOVE, MODIFY, AND COMPLETE TASKS

# This creates an empty list
tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    try:
        tasks.remove(task)
    except ValueError:
        print("Sorry, that task was not found")

def modify_task(task, index):
    tasks[index] = task

def complete_task(task):
    # Add the task to be completed to the completed tasks list
    # this is the difference between remove_task and complete_task
    
    try:
        tasks.remove(task)
    except ValueError:
        print("Sorry, that task was not found")

def find_task_index_by_value(task: str):
    for i in range(len(tasks)):
        # Case insensitive
        if task.lower() == tasks[i].lower():
            return i
    
    # Value was not found in the list
    return -1

def print_tasks():
    for i in range(len(tasks)):
        print(i + 1, tasks[i])

def main():
    while True:
        print("Current Tasks:")
        print_tasks()
        print()

        option = input("What would you like to do?\n1. Add\n2. Remove \n3. Modify\n4. Complete\n5. Exit\nSelect:  ")

        if option == "1":
            task = input("What task would you like to add?\nEnter: ")
            add_task(task)

        elif option == "2":
            task = input("What task would you like to remove?\nEnter:  ")
            remove_task(task)

        elif option == "3":
            task = input("What task would you like to modify?\nEnter:  ")
            task_index = find_task_index_by_value(task)

            if task_index == -1:
                print(task, "was not found in tasks")
                continue
            
            # if found... what to do
            new_task = input("Enter the new task\nEnter:  ")
            modify_task(new_task, task_index)

        elif option == "4":
            task = input("Enter the task to complete\nEnter:  ")
            complete_task(task)

        elif option == "5":
            break
        else:
            print("Invalid Input\n")

    print("Thank you for using our TODO App")

main()