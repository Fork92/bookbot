import sys
from stats import get_num_words
from stats import count_character
from stats import sort_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    sorted_count = sort_dict(count_character(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_count:
        c = entry["char"]
        count = entry["num"]
        print(f"{c}: {count}")


main()
