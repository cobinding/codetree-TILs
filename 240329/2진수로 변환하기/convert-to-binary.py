n=int(input())

ans=str()
while True:
    if n < 1 : break

    if n%2==0:
        ans+='0'
    else:
        ans+='1'

    n//=2

if n==0: print(0)
elif n==1: print(1)
else: print(ans[::-1])