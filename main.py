def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    report = create_sorted_list(char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for character, count in report:
      print(f"The {character} was found {count} in the document")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

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
