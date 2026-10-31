sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]

#Print each sequence with its length
for seq in sequences:
    print(seq, len(seq))    

#Build a list of lengths, then print the average
lengths = [len(seq) for seq in sequences]
number = 0
for n in lengths:
    number = number + n
average = number / len(lengths)
print("Average length:", average)

#Count how many sequences start with ATG
count = 0
for seq in sequences:
    if seq.startswith("ATG"):
        count = count + 1
print("Starts with ATG:", count)

#Print only the sequences longer than 5 bases
print("Sequences longer than 5 bases:")
for seq in sequences:
    if len(seq) > 5:
        print(seq)
else:
    print("No more sequences longer than 5 bases.")

#For each sequence print its GC content (loop inside a loop!)
for seq in sequences:
    Count_G = seq.count('G')
    Count_C = seq.count('C')
    gc = (Count_G + Count_C) / len(seq) * 100
    r_gc = round(gc, 2)
    print(seq, "GC content:", r_gc) 