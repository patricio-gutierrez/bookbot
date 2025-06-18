import sys
from stats import get_num_words, get_chars_dict, transform_dict, sort_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def pretty_print(book_name ,num_words, word_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in word_list:
        if el["word"].isalpha():
            print(f"{el["word"]}: {el["count"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    book_content = get_book_text(book_name) 
    num_words = get_num_words(book_content)
    chars_dict = get_chars_dict(book_content)
    transformed_dict = transform_dict(chars_dict)
    sorted_dict = sort_words(transformed_dict)
    pretty_print(book_name, num_words, sorted_dict)

main()