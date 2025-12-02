def create_codon_dict(file_path):
    path = "/content/data/codons.txt"
    file = open(path)
    rows = file.readlines()
    file.close()
    
    codon_dict = {}
    for row in rows:
      parts = row.strip().split('\t')
      codon = parts[0]
      amino_acid = parts[2]

      codon_dict[codon] = amino_acid

     return codon_dict
