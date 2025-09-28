# main.py

import sys

from stats import (
    count_words,
    count_chars,
    sort_dicts
)

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    word_count = count_words(text)
    chars_count = count_chars(text)
    char_list_stats = sort_dicts(chars_count)

    print_report(path, word_count, char_list_stats)

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(f"Failed to open the file: {e}")

def print_report(path, word_count, char_list_stats):
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {path}...")

    print("-" * 12 + " Word Count " + "-" * 12)
    print(f"Found {word_count} total words")

    print("-" * 12 + " Character Count " + "-" * 12)
    for i in char_list_stats:
        print(f"{i["char"]}: {i["num"]}" )

    print("=" * 12 + " END " + "=" * 12)
    
if __name__ == "__main__":
    main()

