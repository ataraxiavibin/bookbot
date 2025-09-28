# stats.py
#

def count_words(file_contents):
    return len(file_contents.split()) # word_count

def count_chars(file_contents):
    chars_count = {}
    
    for char in file_contents.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_on(items):
    return items["num"]

def sort_dicts(chars_count):
    chars = []
    for char in chars_count:
        if char.isalpha():
            chars.append({"char": char, "num": chars_count[char]})

    chars.sort(reverse=True, key=sort_on)

    return chars
