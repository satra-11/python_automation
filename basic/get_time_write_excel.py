import datetime
import os
from datetime import datetime as dt
from zoneinfo import ZoneInfo

import win32com.client as com

today_naive = datetime.datetime.now()

# naive な datetime オブジェクト
print(today_naive, "      naive_ローカル時間")

# aware な datetime オブジェクト"
today_UTC_aware_2 = today_naive.astimezone(ZoneInfo("UTC"))
print(today_UTC_aware_2, "aware_UTC時間")

today_tokyo = today_UTC_aware_2.astimezone(ZoneInfo("Asia/Tokyo"))
print(today_tokyo, "aware_JST時間")

# aware な datetime オブジェクト ISO表記
iso_time_utc = today_UTC_aware_2.isoformat()
print(iso_time_utc, "iso_time_utc")

iso_time_tokyo = today_tokyo.isoformat()
print(iso_time_tokyo, "iso_time_tokyo")

# Excelに張り付けるための書式
excel_time = dt.strftime(today_naive, ("%Y/%m/%d" "  " "%H:%M:%S"))
print(excel_time, "             Excelに張り付けるための書式")


# プログラムファイルのディレクトリパス（folder_path）の取得
folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス:", folder_path)

# エクセルファイルのパス
excel_file_path = folder_path + os.sep + "Excelシートへの日時の転記.xlsx"
print("エクセルファイルのパス:", excel_file_path)

# エクセルアプリケーションの起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 処理対象シートの指定
wb = app.Workbooks.Open(excel_file_path)
sheet = wb.Worksheets("Sheet1")

sheet.Cells(2, 2).Value = today_naive
sheet.Cells(3, 2).Value = today_UTC_aware_2
sheet.Cells(4, 2).Value = today_tokyo
sheet.Cells(5, 2).Value = iso_time_utc
sheet.Cells(6, 2).Value = iso_time_tokyo
sheet.Cells(7, 2).Value = excel_time
