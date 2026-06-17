import pandas as pd
import glob

# 1. Saare 3 CSV files read kar lo
files = glob.glob('*.csv')
all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

# 2. Sabko ek saath jod do
df = pd.concat(all_data, ignore_index=True)

# 3. Sirf Pink Morsels wali rows rakho
df = df[df['product'] == 'Pink Morsels']

# 4. Sales naya column banao = quantity * price
df['sales'] = df['quantity'] * df['price']

# 5. Sirf Date, Region, sales wale column rakho
final_df = df[['date', 'region', 'sales']]

# 6. output.csv me save kar do
final_df.to_csv('output.csv', index=False)