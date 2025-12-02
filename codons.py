def create_codon_dict(file_path):

  codon_dict = {}

  file = open(path)

  rows = file.readlines()

  file.close()

  for row in rows:
      parts = row.strip().split('\t')

      if len(parts) < 3:
            continue

      codon = parts[0]
      amino_acid = parts[2]

      codon_dict[codon] = amino_acid

  return codon_dict
