import win32com.client as com
import os

folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

input_file_path = folder_path + os.sep + ".." + os.sep + "assets" + os.sep + "HelloPDF.pdf"
print("Wordファイルのパス：", input_file_path)

app = com.Dispatch("Word.Application")
app.Visible = True
app.DisplayAlerts = False

doc = app.Documents.Open(input_file_path)

output_file_path_txt = folder_path + os.sep + "Word_サンプル.txt"
doc.SaveAs(output_file_path_txt, FileFormat=4)

output_file_path_doc = folder_path + os.sep + "Word_サンプル.doc"
doc.SaveAs(output_file_path_doc, FileFormat=0)

output_file_path_doc2 = folder_path + os.sep + "Word_サンプル.docx"
doc.SaveAs(output_file_path_doc2, FileFormat=16)

doc.Close

app.Quit()
