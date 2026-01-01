import sys
from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    words = count_words(book_text)
    characters = count_characters(book_text)
    character_counts = sort_characters_by_count(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in character_counts:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
main()