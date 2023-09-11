import datetime
import time

while True:
    # a=1
    # while a ==1:
    time.sleep(5)

    today_time = datetime.datetime.now()
    today_hour_min = today_time.strftime("%H%M")
    today_hour_min = int(today_hour_min)

    if 900 <= today_hour_min <= 1130:
        print("前場が開いています")

    elif 1250 <= today_hour_min <= 1500:
        print("後場が開いています")

    else:
        print("株式取引の売買立会時間外です")