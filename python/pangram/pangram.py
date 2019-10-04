def is_pangram(sentence):
    if sentence == "" or sentence is None:
      return False
    unique_chars = set()
    for char in sentence.lower():
      if char >= 'a' and char <= 'z':
        unique_chars.add(char)
    if len(unique_chars) == 26:
      return True
    return False
