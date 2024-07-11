a,b=map(int,input().split())
arr=list(range(a,b+1))

# 3,6,9 중 하나가 있는지 확인
def is_369(li):
    cnt=0
    for number in li:
        # 중복 카운팅을 막기 위해 3으로 나눴을 때 0이 아닌 값만 체크
        if number%3!=0:
            number_to_str=str(number)
            for item in number_to_str:
                if item=='3' or item=='6' or item=='9':
                    cnt+=1
    return cnt

# 3의 배수인지 확인
def is_3_mul(li):
    cnt=0
    for i in li:
        if i%3==0:
            cnt+=1
    return cnt


print(is_369(arr)+is_3_mul(arr))