from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# webdrivermanagerを入れた方が良い。ブラウザは頻繁に更新されるため
# seleniumIDEでブラウザ操作を記録できるのでお勧め

# ファイルのダウンロード用にChromeオプションを設定
chrome_options = webdriver.ChromeOptions()
prefs = {
    #webdriverの場所を指定。pythonを複数バージョン動かす場合によい
    "download.default_directory": r"C:\Users\syuzu\desktopdriver\chromedriver.exe",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
chrome_options.add_experimental_option("prefs", prefs)

# WebDriverを初期化
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.aozora.gr.jp/cards/000311/card1974.html#download"

driver.get(url)
time.sleep(1)

# 部分一致のテキストでダウンロードリンクを検索してクリック
driver.find_element(By.PARTIAL_LINK_TEXT, "1974_ruby_6878.zip").click()

# ダウンロードするファイルサイズによって調整する。途中で処理が続くと,tmpファイルが生成される
time.sleep(5)

# 処理が完了したらWebDriverを閉じる
driver.quit()


