m1, d1, m2, d2=map(int,input().split())

# 각 코드마다 몇 일이 있는지를 배열로 저장
num_of_days=[0,31,28,31,30,31,30,31,30,31,31,30,31,30,31]

start_day=num_of_days[m1]-d1
end_day=d2
ans=end_day+start_day+1

if m2-m1 > 1:
    ans += num_of_days[m1:m2+1]

print(ans)