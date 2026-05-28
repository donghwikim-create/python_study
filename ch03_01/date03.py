# 계절 구분하는 프로그램
# 봄 = 3월 ~ 5월
# 여름 = 6월 ~ 8월
# 가을 = 9월 ~ 11월
# 겨울 = 12월 ~ 2월

import datetime

now = datetime.datetime.now()

if 3<= now.month <=5:
    print("현재는 {}월 이므로 봄입니다.".format(
        now.month
    ))

if 6<= now.month <=8:
    print("현재는 {}월 이므로 여름입니다.".format(
        now.month
    ))

if 9<= now.month <=11:
    print("현재는 {}월 이므로 가을입니다.".format(
        now.month
    ))

if 12<= now.month <=2:
    print("현재는 {}월 이므로 겨울입니다.".format(
        now.month
    ))