import pandas as pd

file_path = r'C:\coding_work\GitHub\neurotech_fnir_mind\data\rest15_averaged.csv'

df = pd.read_csv(file_path)

print("Before filtering:")
print(df.head())

df = df.iloc[:, 0:3]

df = df[(abs(df['HbO_avg']) > 1e-07) & (abs(df['HbR_avg']) > 1e-07)]

print("After filtering:")
print(df.head())

df.to_csv(file_path, index=False)