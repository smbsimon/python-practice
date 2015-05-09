def word_count(phrase):
    collection = {}
    split_phrase = phrase.split()

    for i in split_phrase:
        if i not in collection:
            collection[i] = 1
        else:
            collection[i] += 1

    return collection
