from string import maketrans

def to_rna(dna):
    d = "GCTA"
    r = "CGAU"

    transcription = maketrans(d, r)

    return dna.translate(transcription)
