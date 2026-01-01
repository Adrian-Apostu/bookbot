def count_words(text):
    return len(text.split())

def count_characters(text):
    lowercased = text.lower()
    count_characters = {}
    for char in lowercased:
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1
    return count_characters
    
def sort_on(items):
    return items["num"]
    
def sort_characters_by_count(character_counts):
    counts_list = []
    entry = {}
    for char in character_counts:
        if char.isalpha() is False:
            continue
        entry["char"] = char
        entry["num"] = character_counts[char]
        counts_list.append(entry)
        entry = {}
    counts_list.sort(key=sort_on, reverse=True)
    return counts_list