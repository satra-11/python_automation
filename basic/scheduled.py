import datetime
import sys
import time
import schedule

x = 0


def job():
    # xをグローバル宣言
    global x
    x = x + 1
    now_1 = datetime.datetime.now()

    print(x, now_1, "実行中です。")

    match x == 5:
        case True:
            schedule.clear()
            sys.exit()

# 三秒ごとに実施、
schedule.every(3).seconds.do(job)

# 毎時23秒ごとに実施
# schedule.every().minute.at(":23").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
