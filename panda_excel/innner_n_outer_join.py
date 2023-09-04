import pandas as pd

df_1 = pd.read_excel("./../assets/当社の価格表.xlsx")
df_2 = pd.read_excel("./../assets/ライバル店の価格表.xlsx")

df_result_inner = pd.merge(df_1, df_2, how="inner", on=["メニュー名"])
df_result_inner.to_excel("比較結果_inner.xlsx")

df_result_inner = pd.merge(df_1, df_2, how="inner", on=["メニュー名"])
df_result_inner.to_excel("比較結果_inner.xlsx")

# leftは主。rightは従だが。これはleftらしい(ChatGPTによると...。)
df_result_outer = pd.merge(df_1, df_2, how="outer", on=["メニュー名"])
print(df_result_outer)
df_result_outer.to_excel("比較結果_outer.xlsx")