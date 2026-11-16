import pandas as pd
df = pd.read_csv("data/samples.csv")

print(f"Number of samples: {df.shape[0]}")
print(df["organism"].unique())
print(f"Average length: {df['length'].mean():.2f}")
print(df[df["organism"] == "Escherichia coli"])
print(df[(df["gc_content"] > 42) & (df["length"] > 1000)])
print(df.sort_values("gc_content", ascending=False).head(3))

df["length_kb"] = df["length"] / 1000

print(df["organism"].value_counts())