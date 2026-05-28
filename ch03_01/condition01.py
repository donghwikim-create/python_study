# 끝자리로 홀수와 짝수 구분
str_num = input("숫자를 입력해주세요:")

last_num = str_num[-1]

int_num = int(last_num)

# 짝수 구분
if int_num == 0  or int_num == 2 or int_num == 4 or int_num == 6 or int_num == 8:
    print("이 숫자는 짝수입니다.")

# 홀수 구분
if int_num ==1 or int_num == 3 or int_num == 5 or int_num == 7 or int_num == 9:
    print("이 숫자는 홀수입니다.")


 # 처음에는 그냥 정수 타입으로 입력받았지만 마지막 숫자를 알아내려면 정수 타입이 아닌 
 # 문자열로 입력받아 마지막에 정수 타입으로 변경해야함  
