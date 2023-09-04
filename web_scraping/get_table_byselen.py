from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

import csv
import openpyxl

from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

folder_path = os.path.dirname(__file__)
print("ディレクトリパス：", folder_path)

url = "https://mantine.dev/"

driver.get(url)
time.sleep(1)

html = driver.page_source

html_soup = BeautifulSoup(html, "html.parser")

table_all = html_soup.findAll("table", {"class":"mantine-Table-root"})
df_all = pd.read_html(str(table_all))

print(df_all[0])

df_all[0].to_excel("./../assets/get_table.xlsx")