from functools import reduce

def main():
    book_path = 'books/frankenstein.txt' 

    contents = read_book(book_path)
    total_words = count_words(contents)
    word_dict = create_dict(contents)

    generate_report(book_path, total_words, word_dict)

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
        word_dict
        )

def generate_report(book, word_count, word_dict):
    print(f'--- Begin report of {book} ---')
    print(f'{word_count} words found in the document\n')

    dict_list = sorted(
        [{k: v} for k,v in word_dict.items() if k.isalpha()], 
        reverse=True, 
        key=lambda dict: list(dict.values())[0]
        )
    for item in dict_list:
        char = list(item.keys())[0]
        count = list(item.values())[0]
        print(f"The '{char}' character was found {count} times")

    print('--- End report ---')

if __name__ == '__main__':
    main()