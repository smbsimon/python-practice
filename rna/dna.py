def to_rna(dna):
    rna = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

    for i in dna:
        return rna[i]
