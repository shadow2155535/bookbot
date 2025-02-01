def main():
    word_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        

    word_count = 0
    for word in word_list:
        word_count += 1
    
    return word_count



def crdic():
    raw_text = ""
    with open("books/frankenstein.txt") as f:
        raw_text = f.read()

    #for inside a for
    text = raw_text.lower()

    characters = {}

    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters

def mkrep(word_count, characters):
    print ("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    char_list = []
    for char, count in characters.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    
    
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    
    print("--- End report ---")


if __name__ == "__main__":
    word_count = main()

    characters = crdic()

    mkrep(word_count, characters)