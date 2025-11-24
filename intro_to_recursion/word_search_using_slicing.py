words = ['hello', 'world', 'how', 'are', 'you', 'recursion']

word_to_find = input("Enter a word to find: ").lower()

def find_word(word_to_find, copy_words):
    if copy_words == []:
        return None
    
    if word_to_find == copy_words[0]:
        return copy_words[0]
    
    return find_word(word_to_find, copy_words[1::])

found = find_word(word_to_find, words)

if found is not None:
    print("Word found", found)
else:
    print("Word not found")