def hi_there():
    name = "Michael"
    print("Your name is", name)

# name variable does not exists in this
# context - the scope of the 'name' variable
# is unreachable because it lives in the
# hi_there() function
print(name)