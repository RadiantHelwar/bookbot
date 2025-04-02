def your_words_are_numbered(txt_string):
    words = txt_string.split()
    return len(words)

def your_characters_are_numbered(txt_string):
    txt_string = txt_string.lower()
    library = {}
    for character in txt_string:
        if character in library:
            library[character] += 1
        else:
            library[character] = 1
    return library

def sorting(library):
    # Create a list of dictionaries
    char_list = []
    for char, count in library.items():
        char_list.append({"char": char, "count": count})
    
    # Define how to sort
    def sort_on(dict):
        return dict["count"]
    
    # Sort in descending order
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
