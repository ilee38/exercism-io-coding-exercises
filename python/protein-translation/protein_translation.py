AMINOACIDS = { 'AUG' : "Methionine",
               'UUU' : 'Phenylalanine',
               'UUC' : 'Phenylalanine',
               'UUA' :'Leucine',
               'UUG' : 'Leucine',
               'UCU' : 'Serine',
               'UCC' : 'Serine',
               'UCA' : 'Serine',
               'UCG' : 'Serine',
               'UAU' : 'Tyrosine',
               'UAC' : 'Tyrosine',
               'UGU' : 'Cysteine',
               'UGC' : 'Cysteine',
               'UGG' : 'Tryptophan',
               'UAA' : 'STOP',
               'UAG' : 'STOP',
               'UGA' : 'STOP'}

def proteins(strand):
  if len(strand) == 0 or strand is None:
    return []
  result = []
  for i in range(0, len(strand)-2, 3):
    codone = strand[i:i+3]
    if codone in AMINOACIDS:
      if AMINOACIDS[codone] == "STOP":
        return result
      else:
        result.append(AMINOACIDS[codone])
  return result

