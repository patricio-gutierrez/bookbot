def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = count_words(file_contents)
        print(words)

def count_words(book):
    return len(book.split())

main()
