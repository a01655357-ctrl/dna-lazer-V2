# dna-lazer-V2 - Final Version
def analyze_dna(dna):
    dna = dna.upper().strip()
    valid_bases = "ATGC"
    for base in dna:
        if base not in valid_bases:
            return f"Error: {base} is invalid"
    length = len(dna)
    if length == 0:
        return "No DNA entered!"
    a = dna.count('A'); t = dna.count('T')
    g = dna.count('G'); c = dna.count('C')
    gc_percent = ((g + c) / length) * 100
    rna = dna.replace('T', 'U')
    comp_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp = "".join(comp_map[b] for b in dna)
    rev_comp = comp[::-1]
    codon_table = {
        'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
        'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
        'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',
        'UGU':'C','UGC':'C','UGA':'*','UGG':'W',
        'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
        'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
        'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
        'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
        'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
        'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
        'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
        'AGU':'S','AGC':'S','AGA':'R','AGG':'R',
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
        'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
        'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
    }
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        aa = codon_table.get(codon, "-")
        protein += aa
        if aa == "*": break
    print(f"DNA: {dna}")
    print(f"Length: {length} | GC%: {gc_percent:.2f}%")
    print(f"RNA: {rna}")
    print(f"Reverse Complement: {rev_comp}")
    print(f"Protein: {protein}")
    return protein
analyze_dna("ATGCGATAGCTAGCTAGCTAA")
