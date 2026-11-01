# fixed report 

def read_fasta(path):
    sequences = {}
    name = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences


def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return gc


def report(name, seq):
    gc = gc_content(seq)
    print(f"Sequence: {name} length {len(seq)}")
    print(f"  GC content: {gc:.1f}%")
    return gc


sequences = read_fasta("sequences.fasta")

results = {}
for name, seq in sequences.items():
    results[name] = report(name, seq)

average = sum(results.values()) / len(results)
print(f"Average GC: {average:.1f}%")

key = list(sequences.keys())[0]
print("Reference sequence:", sequences[key])