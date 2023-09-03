import pandas as pd

df_1 = pd.read_excel("./../assets/売り上げ_1.xlsx", index_col=0)
df_2 = pd.read_excel("./../assets/売り上げ_2.xlsx", index_col=0)

df_sum_1_2 = pd.merge(df_1, df_2, on=["メニュー名", "現在の価格"])

df_sum_1_2.to_excel("売り上げ集計.xlsx")
