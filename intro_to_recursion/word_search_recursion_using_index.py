words = ['hello', 'world', 'how', 'are', 'you', 'recursion']

word_to_find = input("Enter a word to find: ").lower()

def find_word(word_to_find, n):
    if n >= len(words):
        return None
    
    if word_to_find == words[n]:
        return n
    
    return find_word(word_to_find, n + 1)

found = find_word(word_to_find, 0)

if found is not None:
    print("Word found", words[found])
else:
    print("Word not found")