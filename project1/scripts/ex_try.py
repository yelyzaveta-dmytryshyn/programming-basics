seq = "ATGCCCTAA"

if len(seq) > 5:
    print("A")
elif len(seq) > 3:
    print("B")
else:
    print("C")

if seq.startswith("ATG") and seq.endswith("TAA"):
    print("D")