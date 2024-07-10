import sys;input=sys.stdin.readline

s=input().rstrip()

start,end=0,0

unique_chars=set()
max_length=0


while end<len(s):
    # 중복이 없다면 집합에 추가하고, 오른쪽 포인터 이동
    # 중복이 없으므로 최대 길이 갱신
    if s[end] not in unique_chars:
        unique_chars.add(s[end])
        end+=1
        max_length=max(max_length,end-start+1)
        
    # 중복이 있다면 왼쪽 포인터 이동
    else:
        unique_chars.remove(s[start])
        start+=1
    
print(max_length)