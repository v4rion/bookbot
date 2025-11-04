import sys
from stats import word_counter
from stats import char_counter
from stats import sort_list

def get_books_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_books_text(book_path)
    sorted_list = sort_list(char_counter(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(text)} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
