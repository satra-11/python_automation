from selenium import webdriver
import time
import os
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

url = "https://developer.mozilla.org/ja/docs/Web/CSS/::before"

driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

h1 = soup.find("h1")

print(h1)
print((h1.decode_contents(formatter="html")))
