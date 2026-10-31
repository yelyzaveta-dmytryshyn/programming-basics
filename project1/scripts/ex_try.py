seq = "ATGCGCATG"

def count_bases(seq):
    counts = {}
    for base in seq:
        counts[base] = counts.get(base, 0) + 1
    return counts

def count_g(seq):
    g_count = {}
    for base in seq:
        if base == "G":
            g_count[base] = g_count.get(base, 0) + 1
    return g_count 

print("Base counts:", count_bases(seq))
print("G counts:", count_g(seq))