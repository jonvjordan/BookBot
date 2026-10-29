import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words
from stats import count_characters
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words (text)
    num_chars = count_characters(text)
    sorted_list = chars_dict_to_sorted_list(num_chars)
    print_report(path, num_words, sorted_list)

def print_report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
