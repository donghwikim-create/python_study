# 현재 시간이 오전 오후 구분하는 프로그램
import datetime

now = datetime.datetime.now()

if now.hour > 12:
    print("현재 시간은 {}시 이므로 오후 입니다.".format(
        now.hour
    ))

if now.hour < 12:
    print("현재 시간은 {}시 이므로 오전입니다.".format(
        now.hour
    ))