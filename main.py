# dna-lazer-V2 - Advanced DNA Analyzer
# Author: a01655357-ctrl
# Project V2 - Improved version

def analyze_dna(dna):
    dna = dna.upper().strip()
    
    # التأكد انه DNA صحيح
    valid_bases = "ATGC"
    for base in dna:
        if base not in valid_bases:
            return f"خطأ! الحرف {base} مش من حروف الـ DNA (ATGC)"

    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    gc_percent = ((g_count + c_count) / length * 100) if length > 0 else 0

    # 1. Transcription DNA -> RNA
    rna = dna.replace('T', 'U')

    # 2. Reverse Complement
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement = "".join(complement_map[b] for b in dna)
    reverse_complement = complement[::-1]

    # 3. Translation (بسيط)
    codon_table = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
        'AUG':'M', 'UUU':'F', 'GCU':'A', 'GCC':'A'
    }
    
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        if codon == "AUG":
            protein += "M"
        elif codon in ["UAA", "UAG", "UGA"]:
            protein += "*"
            break
        else:
            protein += "-"

    # النتائج
    print("="*40)
    print(f"🧬 DNA LAZER V2 - ANALYSIS RESULT")
    print("="*40)
    print(f"Sequence: {dna}")
    print(f"Length: {length} bases")
    print(f"A: {a_count} | T: {t_count} | G: {g_count} | C: {c_count}")
    print(f"GC Content: {gc_percent:.2f}%")
    print("-" * 40)
    print(f"RNA (Transcription): {rna}")
    print(f"Reverse Complement: {reverse_complement}")
    print(f"Protein (simplified): {protein if protein else 'No start codon AUG found'}")
    print("="*40)

# شغل البرنامج
if __name__ == "__main__":
    sample_dna = input("دخل تسلسل الـ DNA (مثال: ATGCGTAA): ")
    if not sample_dna:
        sample_dna = "ATGCGATAGCTAGCTAGCTAA"
    analyze_dna(sample_dna)
