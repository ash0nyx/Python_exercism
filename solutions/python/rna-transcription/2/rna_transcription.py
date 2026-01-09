def to_rna(dna_strand):
    translation = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(translation[nucleotide] for nucleotide in dna_strand)