words = ['hello', 'world', 'how', 'are', 'you', 'recursion']

word_to_find = input("Enter a word to find: ").lower()

def find_word(word_to_find):
    for word in words:
        if word.lower() == word_to_find:
            return word
        
    return 

found = find_word(word_to_find)

if found is not None:
    print(f"Word found using loop: {found}")
else:
    print("Word not found")