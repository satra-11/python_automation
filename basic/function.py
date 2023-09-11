def keisan(value_1, value_2):
    tashizan = value_1 + value_2
    kakezan = value_1 * value_2

    return tashizan, kakezan

# 配列みたいに返すことができる
result_1, result_2 = keisan(3,4)
print(result_1, result_2)