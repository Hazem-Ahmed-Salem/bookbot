from stats import num_of_words , num_of_letters,report
import sys


try: 
    report(sys.argv[1])
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
