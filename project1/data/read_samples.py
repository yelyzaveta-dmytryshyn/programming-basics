def average(numbers):
    return sum(numbers) / len(numbers)

gc_content = []

with open('samples.csv', 'r') as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split(',')
        gc = float(parts[1])
        gc_content.append(gc)

print("value with python:", average(gc_content))

import pandas as pd

df = pd.read_csv('samples.csv')
result_pandas = df['gc_content'].mean()

print("value with pandas:", result_pandas)

print(df.describe())