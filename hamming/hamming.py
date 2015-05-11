def distance(a, b):
    hamming = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            hamming += 1
    return hamming
