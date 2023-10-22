import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/Medlytics2023/Week1/master/Datasets/allhypo.train.data"
df = pd.read_csv(url, sep='\t', na_values=['?'])

# Remove non-numeric values and replace NaN values with the median for each column
for column in df.columns:
    if df[column].dtype != 'object':
        median = df[column].median()
        df[column].fillna(median, inplace=True)


# print(dataset.head(20))

# # convert ? to NaN
# dataset[dataset == '?'] = np.nan
# dataset.fillna(dataset.median(), inplace=True)

df.to_csv("cleaned_data_real.csv", index=False)



