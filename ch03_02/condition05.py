# 날짜/시간과 관련된 기능을 가져온다.
import datetime

# 현재 날짜/시간을 구하고
# 쉽게 사용할 수 있게 월을 변수에 저장한다.
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절 확인

if 3 <=month<= 5:
    print("봄입니다")
elif 6 <=month<= 8:
    print("여름입니다")
elif 9 <=month <= 11:
    print("가을입니다")
else:
    print("겨울입니다.")