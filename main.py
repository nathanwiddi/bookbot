import sys

from stats import get_num_words

def main():
    if len(sys.argv) < 2:  # sys.argv[0] is the script name, so 3 means two actual arguments
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    report = create_sorted_list(char_count)
    print("--- Begin report of " + path_to_file + " ---")
    print(f"{num_words} words found in the document")
    for character, count in report:
      print(f"{character}: {count}")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_char_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(char_count):
    return char_count[1]

def create_sorted_list(char_count):
    alpha_dict = {}
    for letter in char_count:
        if letter.isalpha():
            alpha_dict[letter] = char_count[letter]

    sorted_list = sorted(alpha_dict.items(), key=sort_on, reverse=True)
    return sorted_list


main()
