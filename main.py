from functools import reduce

def main():
    book_path = 'books/frankenstein.txt' 

    contents = read_book(book_path)
    # print(contents)

    total_words = count_words(contents)
    # print(total_words)

    word_dict = create_dict(contents)
    # print(word_dict)


def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(contents):
    word_list = contents.split()
    return len(word_list)

def create_dict(text):
    word_dict = {}
    return reduce(
        lambda dict, word: {**dict, word.lower(): dict.get(word.lower(), 0) + 1}, 
        text.lower(),
        word_dict)

if __name__ == '__main__':
    main()