a,b=map(int,input().split())
numbers=list(range(a,b))

# 소수 판별 함수, 소수이면 True return 
def is_prime(n):
    for i in range(2,b):
        if n!=i and n%i==0: return False
    
    return True

sum_prime_number=0
for number in numbers:
    if is_prime(number):
        sum_prime_number+=number

print(sum_prime_number)