import sympy

# 4. 특정 범위 내의 소수 구하기 (이터레이터 반환)
primes = list(sympy.primerange(100, 1000))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

count = len(primes)
print("100부터 1000사이의 소수개수:", count)