sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)

print(len(sequences))
print(len(gene))
print("The first sequence is:", sequences[0], "and the last sequence is:", sequences[-1])
print("The first in gene is:", gene[0], "and the last is:", gene[-1])

sequences.append("AGTTGA")

gene_lenghts = [140, 816, 1023, 567, 3478]
print("The longest gene is:", max(gene_lenghts), "and the shortest gene is:", min(gene_lenghts),"."
       "The average gene length is:", sum(gene_lenghts)/len(gene_lenghts))    

name, chrome, start, stop = gene
print(f"{name} is on {chrome} and is {stop - start} bases long.")

gene[0] = "ERR4"

#Traceback (most recent call last):
#File "/home/lzsav/programming-basics/project1/scripts/seq_stats.py", line 16, in <module>
#gene[0] = "ERR4"
#TypeError: 'tuple' object does not support item assignment