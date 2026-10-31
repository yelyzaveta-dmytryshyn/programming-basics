seq = input("Enter a DNA sequence: ")

#length
if len(seq) < 30:
    print("too short")

#contains N
if "N" in seq:
    print("contains unknown bases")

#GC content
Count_G = seq.count('G')
Count_C = seq.count('C')
gc = (Count_G + Count_C) / len(seq) * 100
if gc < 0.4:
    print("AT rich")
elif gc > 0.6:
    print("GC rich")
else: 
    print("balanced")

if seq.startswith("ATG") and len(seq) % 3 == 0:
    print ("possible ORF")

