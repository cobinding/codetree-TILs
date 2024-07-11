n,m=map(int,input().split())

def get_lcm(n,m):
    lcm=0
    for i in range(max(n,m), 1, -1):
        if n%i==0 and m%i==0:
            n = n//i
            m = m//i 
            lcm+=(i*n*m)
    
    return lcm

print(get_lcm(n,m))