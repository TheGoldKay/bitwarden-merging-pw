import pandas as pd

# Read the CSV file
df = pd.read_csv('BITWARDEN_VAULT.csv')
print(df.columns)
print(f"Num of rows before: {len(df)}")
# Remove duplicates based on two columns 'column1' and 'column2'
df.drop_duplicates(subset=['login_username', 'login_password'], inplace=True)
print(f"Num of rows after: {len(df)}")
# Write the deduplicated data to a new CSV file
df.to_csv('clean.csv', index=False)
