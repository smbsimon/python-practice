def distance(strand1, strand2):
    hamming = 0

    for x, y in zip(strand1, strand2):
        if x != y:
            hamming +=1
    return hamming
