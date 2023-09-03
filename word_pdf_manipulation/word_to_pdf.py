import win32com.client as com
import os

# プログラムファイルのディレクトリパス(folder_path)の取得。つまり、このスクリプト。
folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス:", folder_path)

# os.sepとは"\"のこと。ここにpdfに変換したいファイル名を入れる
word_file_path = folder_path + os.sep + r"Hello_world.docx"
print("Wordファイルパス:", word_file_path)

# wordの起動
app = com.Dispatch("Word.Application")
app.Visible = True
app.DisplayAlerts = False

doc = app.Documents.Open(word_file_path)

pdf_file_path = folder_path + os.sep + "Word_サンプル.pdf"

doc.SaveAs(pdf_file_path, FileFormat=17)

# ドキュメントを閉じる
doc.Close

# wordアプリケーションの終了
app.Quit()