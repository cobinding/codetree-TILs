# 십진수로 변겅
def to_decimal(binary_number):
    number = 0
    n = len(binary_number)-1
    for i in range(n, -1, -1):
        number += 2**(n-i) * binary_number[i]
    
    return number

# 이진수로 변경
def to_binary(decimal_number):
    binary_list = []
    while decimal_number != 0:
        binary_list.append(decimal_number%2)
        decimal_number //= 2

    # 연산한 값을 reverse하여 이진수 도출
    re_binary_list = []
    for i in range(len(binary_list)-1, -1, -1):
        re_binary_list.append(binary_list[i])
    
    return re_binary_list


binary_n = input()
binary_n = list(map(int, binary_n))
decimal_number = to_decimal(binary_n) * 17
# 17배 이후 다시 이진수로
ans = to_binary(decimal_number)
print(''.join(map(str,ans)))