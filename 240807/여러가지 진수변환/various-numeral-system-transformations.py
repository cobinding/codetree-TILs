n, b = map(int, input().split())

number = []
while n != 0:
    number.append(n % b)
    n //= b

for i in range(len(number)-1, -1, -1):
    print(number[i], end = "")