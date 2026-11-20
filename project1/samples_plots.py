import pandas as pd
df = pd.read_csv("data/samples.csv")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["gc_content"], bins=6)
ax.set_xlabel("GC content (%)")
ax.set_ylabel("Number of samples")
ax.set_title("GC content distribution")
fig.savefig("results/gc_hist.png", dpi=150, bbox_inches="tight")
print("Saved figure as gc_hist.png to results")

mean_gc = df.groupby("organism")["gc_content"].mean()
fig, ax = plt.subplots()
ax.bar(mean_gc.index, mean_gc.values)
ax.set_xlabel("Organism")
ax.set_ylabel("Mean GC content (%)")
ax.set_title("Mean GC content per organism")
fig.savefig("results/gc_per_organism.png", dpi=150, bbox_inches="tight")
print("Saved figure as gc_per_organism.png to results")

fig, ax = plt.subplots()
for organism, group in df.groupby("organism"):
    ax.scatter(group["length"], group["gc_content"], label=organism)
ax.legend()
ax.set_xlabel("GC content (%)")
ax.set_ylabel("Length")
ax.set_title("GC content vs length")
fig.savefig("results/length_vs_gc.png", dpi=150, bbox_inches="tight")
print("Saved figure as length_vs_gc.png to results")