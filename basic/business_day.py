import datetime
import os

import win32com.client as com

folder_path = os.path.dirname(__file__)

# エクセルファイルのパス
excel_file_path = folder_path + os.sep + "営業日カレンダー.xlsx"
print("エクセルファイルのパス:", excel_file_path)

# Excelアプリケーションの起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 営業日カレンダー.xlsxを開く
wb = app.Workbooks.Open(excel_file_path)
sheet = wb.Worksheets("Sheet1")

# 本日日付の取得（YYYY-MM-DD）
today_time = datetime.datetime.now()
r_today_time = str(today_time)[0:10]
print(r_today_time)


# 変数定義
# ex_r_no：エクセルの行番号

for ex_r_no in range(3, 9):

    # 営業日カレンダーの日付を読み込む
    excel_date = sheet.Cells(ex_r_no, 3).value
    print(excel_date)

    # 読み込んだ日付を（YYYY-MM-DD）に加工
    r_excel_date = str(excel_date)[0:10]

    # 読み込んだ日の「営業日/休日」の情報を取得
    business_day = sheet.Cells(ex_r_no, 5).value

    # print("日付", r_excel_date, "は、", "営業日情報", business_day, "です。")

    if r_today_time == r_excel_date:

        print("本日は", r_today_time, business_day, "です。")

    else:
        pass
