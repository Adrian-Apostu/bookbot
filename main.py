from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = count_words(book_text)
    print(f"Found {words} total words)")
main()