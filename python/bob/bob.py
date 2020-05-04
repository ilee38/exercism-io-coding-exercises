def response(hey_bob):
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    hey_bob = hey_bob.rstrip()
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

