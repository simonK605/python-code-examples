import pandas as pd

df = pd.DataFrame({
    'colx': [pd.NaT, '2022-01-20', None, '2022-01-21', '2022-01-22']
})

# Make sure the index is sorted
df = df.sort_index()

# Convert the column to datetime
df['colx'] = pd.to_datetime(df['colx'])


print(df)