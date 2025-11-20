# ######################################################
# ######################################################
# How it's done using a loop
for_sum = 0
for i in range(1, 11):
    for_sum += i

print(for_sum)

# ######################################################
# ######################################################
# This version for debugging and seeing the live value
def do_sum(sum, n):
    # base case
    if n == 0:
        # return final value (wind down the stack)
        return sum
    
    # recursive case
    return do_sum(sum + n, n-1)


# start with sum of 0, recur 10 times, first invocation
print(do_sum(0, 10))

# ######################################################
# ######################################################
# This concise version is the way to go 
def sum(n):
    # base case
    if n == 1:
        # return final value (wind down the stack)
        return 1
    
    # recursive case
    return n + sum(n-1)


# start with sum of 0, recur 10 times, first invocation
print(sum(10))