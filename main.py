# Imports
import sys
from stats import your_words_are_numbered
from stats import your_characters_are_numbered
from stats import sorting


#my Code
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print (sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = your_words_are_numbered(text)
    characters = sorting(your_characters_are_numbered(text))

    report = (f"============ BOOKBOT ============\n"
              f"Analyzing book found at books/frankenstein.txt...\n"
              f"----------- Word Count ----------\n"
              f"Found {words} total words\n"
              f"--------- Character Count -------\n")
    for character in characters:
        if character['char'].isalpha():  # Only include alphabetical characters
            report += f"{character['char']}: {character['count']}\n"
    
    report += "============= END ==============="
    
    # Print the report
    print(report)
main()