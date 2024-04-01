num=input()

decimal=0
for i in range(len(num)):
    decimal += int(num[i])*2**(len(num)-i-1)

print(decimal)