phrase = input("Enter a phrase: ")
word_to_find = input("Enter a word to find: ")

"""
Hello World, I am here in Programming Class... and I am not falling asleep just yet.
"""
words = phrase.split()
print(words) # a list of strings

# loop each word at a time
# case insensitive search, because all inputs are now lowercase
count = 0
for word in words:
    if word.lower() == word_to_find.lower():
        count += 1
        print("Word matches so far:", count)

print("Done.", "Total word count:", count)