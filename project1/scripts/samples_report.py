import pandas as pd
df = pd.read_csv("data/samples.csv")

print(f"Number of samples per organism: {df['organism'].value_counts()}")
print(f"Mean GC and mean length per organism:\n{df.groupby('organism')[['gc_content', 'length']].mean()}")

df["length_kb"] = df["length"] / 1000

long_kb = df[df["length_kb"] > 1]
long_kb =long_kb.sort_values("length", ascending=False)
long_kb.to_csv("results/long_kb.csv", index=False)