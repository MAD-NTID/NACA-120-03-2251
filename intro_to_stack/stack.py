# Empty list
stack = []

# Get count of elements in the stack
def size():
    return len(stack)

# Return T if it's empty, False otherwise
def empty():
    return size() == 0

# Insert the new element on top of the stack
# insert() takes care of pushing previous elements
# down the stack
def push(element):
    stack.insert(0, element)

# Get the element at the top if it's not empty
def top():
    if size() == 0:
        return None
    
    return stack[0]
    
# Return the top if not empty and delete from stack
# otherwise, return None
# Python list's pop function takes care of shifting 
# elements back to the top
def pop():
    if size() == 0:
        return None
    
    return stack.pop()


def main():
    # insert 50 pringles potato chips into the tube (the stack)
    PRINGLE = "Chip "

    # Let's put all the chips in the tube using a loop
    for pringle_count in range (1, 51):
        push(f"{PRINGLE} - {pringle_count}")

    print(f"There are {size()} potato chips in the tube")
    print(f"Is it empty? {empty()}")

    # Now let's eat 20 potato chips
    for eat_chip in range (20):
        eaten_chip = pop()
        print(f"I just ate potato {eaten_chip}")

    # We should end up with 30 potato chips
    print(f"There are {size()} potato chips in the tube")
    print(f"Is it empty? {empty()}")

    # Now let's eat 25 potato chips
    for eat_chip in range (25):
        eaten_chip = pop()
        print(f"I just ate potato {eaten_chip}")

    # We should end up with 30 potato chips
    print(f"There are {size()} potato chips in the tube")
    print(f"Is it empty? {empty()}")

    # Let's eat the remaining chips
    for eat_chip in range (6):
        if size() > 0:
            eaten_chip = pop()
            print(f"I just ate potato {eaten_chip}")
        else:
            print("No more chips to eat")
            break

    # We should end up with 30 potato chips
    print(f"There are {size()} potato chips in the tube")
    print(f"Is it empty? {empty()}")

main()