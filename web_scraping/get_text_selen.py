from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Chromeの起動
driver = webdriver.Chrome()


folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

html_sample_file_path = folder_path + os.sep + "tourist_information.html"
print(html_sample_file_path)

url = "https://www.coursera.org/professional-certificates/meta-front-end-developer#courses"


driver.get(url)
time.sleep(5)

print("h1 ヘッダー　第一階層======= ")
h1_elms = driver.find_elements(By.TAG_NAME, "h1")
for h1_elm in h1_elms:
    h1_value = h1_elm.text
    print(h1_value)