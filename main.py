from stats import num_of_words , num_of_letters,report
import sys


try: 
    report(sys.argv[1])
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# words_num = num_of_words("books/frankenstein.txt") 
# char = num_of_letters("books/frankenstein.txt")
# print(f"Found {words_num} total words")
