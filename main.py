def main(num=3):
    book_path = "./books/frankenstein.txt"
    text = get_book(book_path)
    
    print(f"--- Begin report of {book_path}")
    print(count_words(text), "words found in the document\n")
    char_dict = count_char(text)
    for char in char_dict:
        print(f"The '{char}' was found {char_dict[char]} times")
    print("--- End report ---")

def get_book(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    text_count = len(text.split())
    return text_count

def count_char(text):
    char_dict = {}
    for char in text:
        letter = char.lower()
        if letter not in char_dict:
            char_dict[letter] = 0
        char_dict[letter] += 1
    return char_dict

main()
