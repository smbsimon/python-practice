def word_count(phrase):
    dictionary = {}
    split_phrase = phrase.split()

    for i in split_phrase:
        dictionary[i] = split_phrase.count(i)

    return dictionary
