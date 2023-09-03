import win32com.client as com
import os

folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

word_file_path = folder_path + os.sep + "Hello_world.docx"
print("Wordファイルのパス：", word_file_path)

pdf_file_path = folder_path + os.sep + "Word_サンプル.pdf"
print("出力先pdfファイルのパス：",pdf_file_path)

# wordの起動
app = com.Dispatch("Word.Application")
app.Visible = True
app.DisplayAlerts = False

doc = app.Documents.Open(word_file_path)


# 書き込み
doc.Range(0, 1).Text = (
    "令和株式会社" + "\n" + "営業部長　徳川様" + "\n" + "いつもお世話になっております。" + "\n" + "\n"
)

# 文字列の置換
app.Selection.Find.ClearFormatting()
app.Selection.Find.Replacement.ClearFormatting()

app.Selection.Find.Execute(
    FindText="hello",
    MatchCase=False,
    MatchWholeWord=False,
    MatchWildcards=False,
    MatchSoundsLike=False,
    MatchAllWordForms=False,
    Forward=True,
    Wrap=1,
    Format=False,
    ReplaceWith="ハロー",
    Replace=2
)

# 画像ファイルの挿入
image_file_path = folder_path + os.sep + "sample.jpg"

# 検索して画像に置き換える文字列。
app.Selection.Find.Execute("This")
app.Selection.InlineShapes.AddPicture(image_file_path)

doc.SaveAs(pdf_file_path, FileFormat=17)

doc.Close
app.Quit()