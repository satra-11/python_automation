import datetime
import os
from datetime import datetime as dt

import win32com.client as com


def time_record():
    """今の日時をExcelに転記用に加工"""
    today_naive = datetime.datetime.now()  # 今の日時
    excel_time = dt.strftime(today_naive, ("%Y/%m/%d" "  " "%H:%M:%S"))  # Excel用日時
    return excel_time


def keisan(value_1, value_2):
    """掛け算の関数"""
    kakezan = value_1 * value_2
    return kakezan


# 以下にサンプルプログラム基準のエクセルファイルパスを定義する。
# プログラムファイルのディレクトリパス（folder_path）の取得
folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス:", folder_path)

# エクセルファイルのパス
excel_file_path = folder_path + os.sep + "１回目の作業シート.xlsx"
print("エクセルファイルのパス:", excel_file_path)

# エクセルアプリケーションの起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 処理対象シートの指定
wb = app.Workbooks.Open(excel_file_path)
sheet = wb.Worksheets("Sheet1")


# セルの行数を変数（y）で定義する
for y in range(5, 13):
    print(y)

    price = sheet.Cells(y, 3).Value
    quantity = sheet.Cells(y, 4).Value

    print(price, type(price))
    print(quantity, type(quantity))

    sales_amount = keisan(value_1=price, value_2=quantity)

    sheet.Cells(y, 5).Value = sales_amount
    sheet.Cells(y, 6).Value = "完了"

    python_excel_time = time_record()
    sheet.Cells(y, 7).Value = python_excel_time
