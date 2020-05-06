def decode(string):
    count = ""
    decoded = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == "":
                decoded += char
            else:
                for i in range(int(count)):
                    decoded += char
            count = ""
    return decoded


def encode(string):
    if len(string) < 1:
        return string
    encoded = ""
    curr_char = string[0]
    char_count = 1
    for next_char in string[1:]:
        if next_char == curr_char:
            char_count += 1
        else:
            encoded = _append_chars(encoded, char_count, curr_char)
            char_count = 1
        curr_char = next_char
    #include last char(s) left after the loop
    encoded = _append_chars(encoded, char_count, curr_char)
    return encoded


def _append_chars(curr_str, count, char):
    """ Utility function: appends characters based on count
    """
    if count > 1:
        curr_str += (str(count) + char)
    else:
        curr_str += char
    return curr_str
