seq = "ATGCTACGATGCTGCATGCATCGTAGCATGCTAG" 

#seq length and GC content
seq_length = len(seq)
print("Sequence Length:", seq_length)
Count_G = seq.count('G')
Count_C = seq.count('C')
gc = (Count_G + Count_C) / seq_length * 100
print("GC:", gc, "%")

#First and last codon
first_codon = seq[0:3]
last_codon = seq[-3:]
print("First Codon:", first_codon)
print("Last Codon:", last_codon)

#RNA version
seq_RNA = seq.replace('T', 'U')
print("RNA Sequence:", seq_RNA)

#Reverse complement
complement = seq.replace("A", "t").replace("T", "a")
complement = complement.replace("G", "c").replace("C", "g")
rev_comp = complement.upper()[::-1]
print("Reverse Complement:", rev_comp)

#Start codon
start = seq.startswith("ATG")
print("Starts with ATG:", start)