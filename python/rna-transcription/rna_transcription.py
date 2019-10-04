complements = {'G': 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

def to_rna(dna_strand):
  if dna_strand == "" or dna_strand is None:
    return ""
  return "".join(complements[i] for i in dna_strand)