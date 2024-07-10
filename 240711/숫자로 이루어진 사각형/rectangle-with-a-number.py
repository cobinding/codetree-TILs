n=int(input())

number=0
for _ in range(n):
    for _ in range(n):
        number+=1
        if number>=10: number-=9
        print(number, end=" ")
    print()