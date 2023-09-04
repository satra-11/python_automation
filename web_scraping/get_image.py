from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()

folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス:", folder_path)

url = "https://mantine.dev/"

driver.get(url)
time.sleep(1)

img_elements = driver.find_elements(By.TAG_NAME, "img")

y = -1
for i in range(len(img_elements)):
    y = y + 1
    png_data = driver.find_elements(By.TAG_NAME, "img")[y].screenshot_as_png
    time.sleep(1)

    x = y + 1
    str_x = str(x)

    # ループを回しているが全て同じファイルに保存されるため、最後の写真だけ残る
    file_path = r".\..\assets\gallery.png"

    with open(file_path, "wb") as f:
        f.write(png_data)

# 最後に残るのはこれ
driver.save_screenshot(r".\..\assets\gallery.png")
