import pandas as pd
df_json = pd.read_json('sample.json')
df_json.to_excel('output.xlsx')