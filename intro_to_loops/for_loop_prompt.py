start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
sum = 0

for i in range(start, end):
    sum = sum + i

print(f"Total sum from {start} to {end} is {sum}")