from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = count_words(book_text)
    characters = count_characters(book_text)
    charachter_counts = sort_characters_by_count(characters)
    result = """
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""" + "\n"
    for entry in charachter_counts:
        result += f"{entry['char']}: {entry['num']}\n"
    result += """
============= END ==============="""
    print(result)
main()