def find_duplicates(string: str):
    if not string:
        return None

    chars = dict()
    duplicated_chars = dict()
    for char in string:
        # Check if char was never seen once
        if not chars.get(char):
            chars[char] = char
        else:
            # Check if char was never seen twice
            if not duplicated_chars.get(char):
                duplicated_chars[char] = char

    if not duplicated_chars:
        return None

    return ",".join(duplicated_chars.keys())
