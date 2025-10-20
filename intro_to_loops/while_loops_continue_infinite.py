count = -1

while True:
    count += 1

    # print only even numbers
    if count % 2 == 0:
        print(count)
        continue # goes back to the top

    if count >= 1000:
        break

print("Completed Printing Event Numbers")