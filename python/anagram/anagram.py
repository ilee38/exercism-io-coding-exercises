def find_anagrams(word, candidates):
    anagrams = []
    for w in candidates:
        if len(w) == len(word) and w.lower() != word.lower():
           if sorted(w.lower()) == sorted(word.lower()):
               anagrams.append(w)
    return anagrams


    """ The solution below only fails 1 test:
        when the words have repeated letters. e.g. "tapper" and "patter"
        The reason is that the set keeps unique elements. So, with the
        two words above, if we eliminate the repeated "p" and "t", they
        do make an anagram, but that's incorrect
    """
    # A = set(word.lower())
    # for w in candidates:
    #     if len(w) == len(word) and w.lower() != word.lower():
    #         B = set(w.lower())
    #         C = A - B
    #         if len(C) == 0:
    #             anagrams.append(w)
    # return anagrams