def to_rna(dna_strand):
    TRANSLATION = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(TRANSLATION)