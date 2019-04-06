def add_word_to_cloud(word_count, word):
    if word in word_count:
        word_count[word] = 1 + word_count[word]

    elif word.lower() in word_count:
        word_count[word.lower()] = 1 + word_count[word.lower()]

    elif word.capitalize() in word_count:
        word_count[word.lower()] = 1
        word_count[word.lower()] = (
            word_count[word.lower()] + word_count[word.capitalize()]
        )
        del word_count[word.capitalize()]

    else:
        word_count[word] = 1


def word_cloud(string):
    word_count = dict()
    word = ""

    for char in string:
        # Check for characters to join composed words
        if word and char in ["-", "'"]:
            word += char
        # Check for alphabetic characters
        elif char.isalpha():
            word += char
        # Check for end of word
        elif word:
            add_word_to_cloud(word_count, word)
            word = ""

    # Add last word, if any
    if word:
        add_word_to_cloud(word_count, word)

    return word_count


if __name__ == "__main__":
    word_count = word_cloud("Chocolate cake for dinner and chocolate cake for dessert")
    print(word_count)
