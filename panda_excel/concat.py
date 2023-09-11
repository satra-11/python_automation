import pandas as pd

df_1 = pd.read_excel("./../assets/registration_information_1.xlsx", index_col=0)
df_2 = pd.read_excel("./../assets/registration_information_2.xlsx", index_col=0)

# 横にくっつけたい場合
df_result = pd.concat([df_1, df_2], axis=1)
# df_result = pd.concat([df_1, df_2])
print(df_result)
df_result.to_excel("結合結果2.xlsx")