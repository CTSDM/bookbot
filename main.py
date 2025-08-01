import sys
from stats import get_book_text, get_num_words, get_characters_information


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(f"./{filepath}")
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${filepath}.")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters_info = get_characters_information(text)
    for c in characters_info:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["num"]}")


main()
