def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    book_words = count_words(book_text)
    characters = count_characters(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def count_characters(book):
    word_dict = {}
    for word in book:
        for character in word.lower():
            if character not in word_dict:
                word_dict[character] = 1
            else:
                word_dict[character] += 1
    return word_dict

def count_words(book):
    return len(book.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
