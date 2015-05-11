def distance(a, b):
    hamming = 0

    for a, b in zip(a, b):
        if a != b:
            hamming +=1
    return hamming
