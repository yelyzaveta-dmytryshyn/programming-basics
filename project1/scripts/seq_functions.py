def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    gc = gc_count / len(seq) * 100
    r_gc = round(gc, 2)
    return r_gc

def reverse_complement(seq):
    complment_gc = seq.replace("G", "c").replace("C", "g")
    complment_at = complment_gc.replace("A", "t").replace("T", "a")
    rev_comp = complment_at[::-1].upper()
    return rev_comp

def is_usable(seq, min_lenght=30):
    if len(seq) > min_lenght and "N" not in seq:
        return True
    else:
        return False 

def first_atg(seq):
    return seq.find("ATG")

seq = input("Enter a sequence: ")

print("GC content:", gc_content(seq))
print("Reverse complement:", reverse_complement(seq))
print("Sequence is usable:", is_usable(seq))
print("Position of ATG:", first_atg(seq))