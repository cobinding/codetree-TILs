n=int(input())

# 1. 짝수인지 검토
def is_even(n): 
    if n%2 == 0: flag=True
    else: flag=False
    return flag

# 2. 5의 배수인지 검토
def is_sum_mul_5(n):
    str_n=str(n)

    total=0
    for item in str_n:
        total+=int(item)
    
    if total%5 == 0: return "Yes"
    else: return "No"

is_even_true = is_even(n)
print("No") if not is_even_true else print(is_sum_mul_5(n))

### 각 자리의 숫자의 합 
### n//10 + n%10
### 두 자리 수니까 위처럼 가능