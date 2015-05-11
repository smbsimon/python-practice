def distance(strand1, strand2):
    hamming = 0

    for a, b in zip(strand1, strand2):
        if a != b:
            hamming +=1
    return hamming
