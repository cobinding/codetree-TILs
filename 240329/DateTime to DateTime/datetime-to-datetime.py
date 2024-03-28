d,h,m=map(int,input().split())


if d < 11 :
    print(-1)
else:
    day=(d-11)*24*60
    hour=abs(h-11)*60
    minute=abs(m-11)
    
    print(day+hour+minute)