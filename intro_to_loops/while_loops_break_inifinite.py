count = 0

while True:
    print("This will print forever...")
    count += 1

    # manual break from loop
    if count == 1000:
        break

print("Total Count:", count)