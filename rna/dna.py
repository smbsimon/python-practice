def to_rna(dna):
    rna = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

    return ''.join(rna[i] for i in dna)
