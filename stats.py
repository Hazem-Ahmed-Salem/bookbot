def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
    
def num_of_words(path):
    string = get_book_text(path)
    words = string.split()
    return len(words)

def num_of_letters(path):
    string = get_book_text(path).lower()
    letters = {}
    for letter in string:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        continue
    return letters

def sort_on(items):
    return items["num"]

def report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    num_word = num_of_words(path)
    characters = num_of_letters(path)
    result_of_char = [{"char":char,"num":characters[char]} for (char) in characters]
    result_of_char.sort(reverse=True,key=sort_on)
    
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    
    for i in result_of_char:
        print(f"{i["char"]}: {i["num"]}")
    
    print("============= END ===============")
    return 0