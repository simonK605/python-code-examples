import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}

df = pd.DataFrame(data)

df['C'] = df[['A', 'B']].sum(axis=1)

print(df)