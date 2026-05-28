# 날짜 시간 모듈을 가져온다
import datetime

# 현재 시간을 now라는 변수에 저장
now = datetime.datetime.now()

# 포멧 함수를 활용해 현재 시간을 한줄로 출력
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))