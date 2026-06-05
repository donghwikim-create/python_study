# 변수 내부에 접근하는 것 --> 참조

# 변수를 선언합니다.
counter = 0

# 함수를 선언합니다.
def fibonacci(n):
    counter+=1
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fibonacci(n-1) + fibonacci(n-2)
    
# 함수를 호출합니다.
print(fibonacci(10))
