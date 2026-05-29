# list_a = [0, 1, 2, 3, 4, 5, 6, 7]
# print(list_a)

# list_a.extend(list_a) # list_a라는 요소를 더하기
# print(list_a)
# list_a.append(10) # 마지막에 요소 추가
# list_a.insert(3, 0) # 3번 위치에 0 이라는 값 추가
# list_a.remove(3) # list_a에서 3이라는 값 제거
# list_a.pop(3) # 3번 인덱스 값 제거, 값이 없을경우 마지막 요소 제거
# list_a.clear # 모든 요소 제거

# -----------------------------------

# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for number in numbers:
#     if number >= 100:
#         print("- 100 이상의 수:", number)

# for number in numbers:
#     if number % 2 == 1:
#         print("{}는 홀수입니다.".format(number))
#     else:
#         print("{}는 짝수입니다.".format(number))

# for number in numbers:
#     if 100<=number<=999:
#         print("{}는 3 자릿수입니다.".format(number))
#     elif 10<=number<=99:
#         print("{}는 2 자릿수입니다.".format(number))
#     elif 1<=number<=9:
#         print("{}는 1 자릿수입니다.".format(number))

# -----------

# list_of_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [8, 9]
# ]

# for element in list_of_list:
#     for element_of_element in element:
#         print(element_of_element)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]


for number in numbers:
    output[(number-1)%3].append(number) 
print(output)

# 나머지 구할때 앞에 숫자가 뒤에 숫자보다 작으면 그 숫자 그대로 나온다.
# ex) 1 % 3 == 1
# ex) 0 % 3 == 0