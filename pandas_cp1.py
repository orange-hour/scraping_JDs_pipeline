import pandas as pd

df = pd.read_csv("/Users/orangehour/projects/scraping_pipeline/out.csv")
print("원본 데이터:", df.shape)
print("column별 데이터 갯수", df.count())

df_clean = df.fillna('NaN')

# Removing newline character from string values
df_clean.replace('\n', ' ', regex=True, inplace=True)

df_clean.to_csv("/Users/orangehour/projects/scraping_pipeline/out_clean_replaced.csv", sep='|', na_rep='NaN', index = False)


