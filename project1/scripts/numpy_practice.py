import pandas as pd
df = pd.read_csv("data/samples.csv")

import numpy as np

ln = df["length"].to_numpy()
ln_arr = np.array(ln)

print("Mean:", ln_arr.mean().round(2))
print("Median:", np.median(ln_arr))
print("SD:", ln_arr.std().round(2))

ln_kb = ln_arr / 1000
ln_count = (ln > 1000).sum()
print("Longer than 1000 bp:", ln_count)

# Mean: 1343.33
# Median: 1270.0
# Mean is bigger than median, which means the distribution is right-skewed.

print(np.percentile(ln_arr, 90))