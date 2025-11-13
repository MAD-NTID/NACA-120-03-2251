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

def main():
    for print_num in range(5):
        enqueue(f"Print Job {print_num}")

    print(f"There are {size()} print jobs for the printer")

    for print_num in range(2):
        printed_job = dequeue()
        print(f"Job printed: '{printed_job}'")

    print(f"There are {size()} print jobs for the printer")

    for print_num in range(size()):
        printed_job = dequeue()
        print(f"Job printed: '{printed_job}'")

    print(f"There are {size()} print jobs for the printer")
main()