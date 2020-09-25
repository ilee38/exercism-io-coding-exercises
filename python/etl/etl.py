def transform(legacy_data):
    data = {}
    scores = legacy_data.keys()
    for score in scores:
        for letter in legacy_data[score]:
            data[letter.lower()] = score
    return data
