# def mul(*values):
#     output = 1
#     for value in values:
#         output *= value
    
#     return output

# print(mul(5, 7, 9, 10))

def function(*value, valueA, valueB): # 가변 매개변수 뒤에는 일반 매개변수가 올수가 없다. 
    pass                              # 왜냐하면 어디까지가 가변 매개변수 인지 모르기 때문에

function(1, 2, 3, 4, 5)