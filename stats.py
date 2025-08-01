def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_characters_count(text):
    characters = list(text.lower())
    characters_unique = set(characters)
    characters_count = {x: characters.count(x) for x in characters_unique}
    return characters_count


def get_characters_information(text):
    characters = []
    characters_count = get_characters_count(text)
    for character, count in characters_count.items():
        characters.append({"char": character, "num": count})
    characters.sort(reverse=True, key=sort_on)
    return characters


def sort_on(items):
    return items["num"]
