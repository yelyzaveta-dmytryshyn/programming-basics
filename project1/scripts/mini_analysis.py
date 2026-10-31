sequences = ["ATGCGCTA", "GGC", "ATGGGCCCTAAA", "TTANNNGC", "ATGAAATTTGGG"]

# Total number of sequences and total number of bases
total_sequences = len(sequences)
total_bases = sum(len(seq) for seq in sequences)
print("Total number of sequences:", total_sequences)
print("Total number of bases:", total_bases)

# Length, GC content, start codon
for seq in sequences:
    length = len(seq)
    gc = (seq.count('G') + seq.count('C')) / length * 100
    r_gc = round(gc, 2)
    start_codon = seq.startswith("ATG")
    print(f"Sequence: {seq}, Length: {length}, GC Content: {r_gc}%, Start codon: {start_codon}")

# Count usable sequences: len(seq) > 5 and no N
usable = 0
for seq in sequences:
    lenght = len(seq)
    if lenght > 5 and 'N' not in seq:
        usable = usable + 1
print("Usable sequences:", usable)

# The longest sequence (if tied, the first one) and its codons, one per line
longest_seq = sequences[0]
for seq in sequences:
    if len(seq) > len(longest_seq):
        longest_seq = seq
print("Longest sequence:", longest_seq)

for i in range(0, len(longest_seq), 3):
    print(longest_seq[i : i + 3])

# Final line: X of Y sequences usable 
print(f"{usable} of {total_sequences} sequences usable")