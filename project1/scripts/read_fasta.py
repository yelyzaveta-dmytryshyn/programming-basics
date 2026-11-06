with open("data/sequences.fasta") as f:
    n_lines = 0
    n_headers = 0
    for line in f:
        n_lines += 1
        if line.startswith(">"):
            n_headers += 1

print(n_lines, n_headers)