# 함수를 선언합니다.
def factorial(n):
    # 변수를 선언합니다.
    output = 1
    for i in range(1, n+1):
        output *= i
    
    return output

print("1!", factorial(1))
print("2!", factorial(2))
print("3!", factorial(3))
print("4!", factorial(4))
print("5!", factorial(5))