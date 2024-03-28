n=int(input())

ans=str()
while True:
    if n < 1 : break

    if n%2==0:
        ans+='0'
    else:
        ans+='1'

    n//=2

print(ans[::-1])