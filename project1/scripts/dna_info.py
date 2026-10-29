seq = "AGCGTGACACAGCTACGACGACAGATCAGCATGTCAGTTAGCATG"
seq_length = len(seq)
print("Sequence Length:", seq_length)
Count_G = seq.count('G')
Count_C = seq.count('C')
gc = (Count_G + Count_C) / seq_length * 100
print("GC:", gc, "%")

seq = input("Enter a DNA sequence: ")
seq_length = len(seq)
print("Sequence Length:", seq_length)
Count_G = seq.count('G')
Count_C = seq.count('C')
gc = (Count_G + Count_C) / seq_length * 100
r_gc = round(gc, 2)
print("GC:", r_gc, "%")